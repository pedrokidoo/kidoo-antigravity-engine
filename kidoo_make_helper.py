# -*- coding: utf-8 -*-
"""
KIDOO HUB — MICROSERVIÇO AUXILIAR ANTIGRAVITY PARA O MAKE.COM (kidoo_make_helper.py)
Entrega 2 da Arquitetura Híbrida:
1. Buffer Anti-Picote (Debounce de 10s para WhatsApp/Z-API)
2. Trava de Intervenção Humana (fromMe = True pausa IA e marca MODO_HUMANO)
3. Sincronização Bidirecional Nativa com o CRM do Erick na Vercel
"""

import os
import sys
import asyncio
import datetime
import json
import uuid
import requests
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, BackgroundTasks, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import gspread

sys.stdout.reconfigure(encoding='utf-8')

# Configurações de Ambiente
CREDENCIAIS_GOOGLE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", r"C:\Users\pedro\OneDrive\Desktop\kidoo\Json kidoo\kidoo-hub-492476e23d24.json")
SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID", "1PRprGhbag7oxvoIG_zrDjXQSupadKIgBguMinkdHzrg")
CRM_BASE_URL = os.getenv("KIDOO_CRM_URL", "https://crm-kidoo.vercel.app")
CRM_WEBHOOK_SECRET = os.getenv("KIDOO_CRM_WEBHOOK_SECRET", "kidoo-local-webhook-secret-24")
MAKE_CENARIO_2_WEBHOOK = os.getenv("MAKE_CENARIO_2_WEBHOOK_URL", "")

app = FastAPI(
    title="Kidoo Hub - Antigravity Make Helper",
    description="Microserviço de Debounce Anti-Picote, Memória e Sync CRM para Make.com",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ESTRUTURA DO BUFFER ANTI-PICOTE (DEBOUNCE 10s)
# -----------------------------------------------------------------------------
class MessageBuffer:
    def __init__(self):
        self.buffers: Dict[str, Dict[str, Any]] = {}
        self.locks: Dict[str, asyncio.Lock] = {}

    def get_lock(self, phone: str) -> asyncio.Lock:
        if phone not in self.locks:
            self.locks[phone] = asyncio.Lock()
        return self.locks[phone]

buffer_manager = MessageBuffer()

# -----------------------------------------------------------------------------
# FUNÇÕES DE GOOGLE SHEETS & CRM SYNC
# -----------------------------------------------------------------------------
def set_modo_humano_na_planilha(telefone: str, ativo: bool = True):
    """Marca a coluna MODO_HUMANO como TRUE quando um sócio digita pelo celular."""
    try:
        gc = gspread.service_account(filename=CREDENCIAIS_GOOGLE)
        sh = gc.open_by_key(SPREADSHEET_ID)
        ws = sh.worksheet("LEADS_INBOUND_ENRIQUECIDOS")
        
        # Localizar coluna MODO_HUMANO e coluna Contato/Telefone
        headers = ws.row_values(2)
        idx_modo_humano = headers.index("MODO_HUMANO") + 1 if "MODO_HUMANO" in headers else 18
        
        # Procurar telefone na planilha
        records = ws.get_all_values()
        for r_idx, row in enumerate(records[2:], start=3):
            # Procura o número nas colunas de contato ou histórico
            row_str = " ".join(row)
            limpo_tel = "".join(filter(str.isdigit, telefone))[-8:]
            if limpo_tel in row_str:
                ws.update_cell(r_idx, idx_modo_humano, "TRUE" if ativo else "FALSE")
                print(f"🔒 [MODO HUMANO] Ativado para o telefone {telefone} na linha {r_idx}")
                return True
        return False
    except Exception as e:
        print(f"⚠️ Erro ao atualizar Modo Humano na planilha: {e}")
        return False

def disparar_para_crm_vercel(payload: dict) -> dict:
    """Dispara lead enriquecido diretamente para o endpoint oficial do CRM do Erick."""
    endpoint = f"{CRM_BASE_URL.rstrip('/')}/api/v1/webhooks/antigravity"
    headers = {
        "x-webhook-secret": CRM_WEBHOOK_SECRET,
        "Content-Type": "application/json"
    }
    try:
        resp = requests.post(endpoint, json=payload, headers=headers, timeout=10)
        return {"status": resp.status_code, "body": resp.json() if resp.status_code in [200, 201] else resp.text}
    except Exception as e:
        return {"status": 500, "erro": str(e)}

# -----------------------------------------------------------------------------
# WORKER ASSÍNCRONO: DEBOUNCE E DISPARO AO MAKE
# -----------------------------------------------------------------------------
async def agendar_debounce_e_disparo(phone: str, delay_seconds: int = 10):
    """Aguarda o buffer estabilizar e dispara para o Make.com."""
    await asyncio.sleep(delay_seconds)
    
    lock = buffer_manager.get_lock(phone)
    async with lock:
        entry = buffer_manager.buffers.get(phone)
        if not entry:
            return
            
        tempo_passado = (datetime.datetime.now() - entry["ultimo_toque"]).total_seconds()
        # Se recebeu nova mensagem no meio do caminho, deixa o timer mais novo disparar
        if tempo_passado < (delay_seconds - 0.5):
            return
            
        dados_finais = buffer_manager.buffers.pop(phone, None)
        
    if not dados_finais:
        return
        
    # Unificar todas as mensagens de texto picadas
    mensagens = dados_finais["mensagens"]
    texto_unificado = "\n".join(mensagens).strip()
    
    payload_consolidado = {
        "event_id": f"zapi-{uuid.uuid4().hex[:10]}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "phone": phone,
        "sender_name": dados_finais.get("sender_name", ""),
        "tipo_mensagem": dados_finais.get("tipo", "text"),
        "mensagem_unificada": texto_unificado,
        "audio_url": dados_finais.get("audio_url"),
        "total_partes_agrupadas": len(mensagens)
    }
    
    print(f"\n🚀 [DEBOUNCE CONCLUÍDO] Telefone {phone}: {len(mensagens)} partes consolidadas!")
    print(f"📝 Conteúdo consolidado:\n{texto_unificado}")
    
    # Se houver webhook do Make configurado, envia
    webhook_target = MAKE_CENARIO_2_WEBHOOK or os.getenv("MAKE_CENARIO_2_WEBHOOK_URL")
    if webhook_target:
        try:
            r = requests.post(webhook_target, json=payload_consolidado, timeout=10)
            print(f"📡 Disparado para Make.com! Status: {r.status_code}")
        except Exception as e:
            print(f"❌ Falha ao enviar para Make.com: {e}")

# -----------------------------------------------------------------------------
# ENDPOINT: RECEPÇÃO DE WEBHOOK DA Z-API / WHATSAPP
# -----------------------------------------------------------------------------
@app.post("/webhook/debounce-whatsapp")
async def webhook_debounce_whatsapp(request: Request, bg_tasks: BackgroundTasks):
    """
    Recebe evento da Z-API.
    1. Verifica fromMe (Intervenção Humana).
    2. Agrupa mensagens enviadas pelo mesmo lead em uma janela de 10 segundos.
    """
    try:
        body = await request.json()
    except Exception:
        body = {}
        
    # Extrair campos da Z-API ou Evolution API
    phone = body.get("phone") or body.get("sender") or body.get("key", {}).get("remoteJid", "")
    phone = phone.replace("@s.whatsapp.net", "").replace("@c.us", "").strip()
    
    is_from_me = body.get("fromMe", False) or body.get("key", {}).get("fromMe", False)
    
    # Se a mensagem foi enviada pelo próprio número da Kidoo (Intervenção Humana de Pedro, Arthur ou Erick)
    if is_from_me:
        print(f"🛑 [INTERVENÇÃO HUMANA DETECTADA] Mensagem manual no WhatsApp para {phone}. Pausando IA.")
        bg_tasks.add_task(set_modo_humano_na_planilha, phone, True)
        return {
            "status": "human_intervention_detected",
            "message": "Mensagem enviada por sócio humano. Automação pausada.",
            "phone": phone
        }
        
    # Extração do conteúdo (Texto ou Áudio)
    texto = body.get("text", {}).get("message") or body.get("body") or body.get("message", {}).get("conversation") or ""
    audio_url = body.get("audio", {}).get("audioUrl") or body.get("audioUrl") or None
    sender_name = body.get("senderName") or body.get("pushName") or "Lead WhatsApp"
    
    tipo = "audio" if audio_url else "text"
    if not texto and not audio_url:
        return {"status": "ignored", "reason": "empty_content"}
        
    # Adicionar ao buffer de 10 segundos
    lock = buffer_manager.get_lock(phone)
    async with lock:
        now = datetime.datetime.now()
        if phone not in buffer_manager.buffers:
            buffer_manager.buffers[phone] = {
                "phone": phone,
                "sender_name": sender_name,
                "mensagens": [],
                "tipo": tipo,
                "audio_url": audio_url,
                "primeiro_toque": now,
                "ultimo_toque": now
            }
        
        if texto:
            buffer_manager.buffers[phone]["mensagens"].append(texto)
        if audio_url:
            buffer_manager.buffers[phone]["audio_url"] = audio_url
            buffer_manager.buffers[phone]["tipo"] = "audio"
            
        buffer_manager.buffers[phone]["ultimo_toque"] = now
        
    # Inicia a contagem regressiva de 10 segundos em background
    bg_tasks.add_task(agendar_debounce_e_disparo, phone, 10)
    
    return {
        "status": "buffering",
        "phone": phone,
        "window_seconds": 10
    }

# -----------------------------------------------------------------------------
# ENDPOINT: SYNC DIRETO COM O CRM DA VERCEL
# -----------------------------------------------------------------------------
class SyncLeadInput(BaseModel):
    empresa: str
    nicho: str
    faturamento_str: str
    contato_nome: str
    contato_telefone: str
    contato_email: Optional[str] = None
    nicho_profundo: str
    dor_especifica: str
    solucao_arquitetada: str
    suggested_setup: float
    suggested_mrr: float
    gancho_vendas: str

@app.post("/crm/sync-lead")
async def sync_lead_endpoint(data: SyncLeadInput):
    """Sincroniza imediatamente o lead enriquecido com o CRM da Vercel."""
    payload = {
        "event_id": f"ag-{uuid.uuid4().hex[:10]}",
        "event_type": "lead.enriched",
        "company": {
            "name": data.empresa,
            "industry": data.nicho,
            "estimated_monthly_revenue": 150000.0
        },
        "contact": {
            "name": data.contato_nome,
            "phone": data.contato_telefone,
            "email": data.contato_email
        },
        "diagnostic": {
            "deep_niche": data.nicho_profundo,
            "specific_pain": data.dor_especifica,
            "proposed_solution": data.solucao_arquitetada,
            "suggested_setup": data.suggested_setup,
            "suggested_mrr": data.suggested_mrr,
            "opening_hook": data.gancho_vendas
        },
        "source": "antigravity"
    }
    
    res = disparar_para_crm_vercel(payload)
    if res.get("status") not in [200, 201]:
        raise HTTPException(status_code=500, detail=res)
    return res

@app.get("/health")
def health():
    return {
        "status": "online",
        "service": "kidoo_make_helper",
        "crm_url": CRM_BASE_URL,
        "spreadsheet_id": SPREADSHEET_ID
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("kidoo_make_helper:app", host="0.0.0.0", port=8001, reload=True)
