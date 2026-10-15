import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import os
import sys
import json
import re
import datetime
from typing import Optional, List

sys.stdout.reconfigure(encoding='utf-8')
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import google.generativeai as genai
import gspread
import uvicorn

from cnpj_service import consultar_cnpj_brasilapi, limpar_cnpj
from kidoo_crm_client import disparar_lead_para_crm_kidoo

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Configurações do Google Sheets & CRM
CREDENCIAIS_GOOGLE_PATH = r"C:\Users\pedro\OneDrive\Desktop\kidoo\Json kidoo\kidoo-hub-492476e23d24.json"
GOOGLE_SHEET_ID = "1PRprGhbag7oxvoIG_zrDjXQSupadKIgBguMinkdHzrg"
CRM_BASE_URL = os.getenv("KIDOO_CRM_URL", "https://crm-kidoo.vercel.app")
CRM_WEBHOOK_SECRET = os.getenv("KIDOO_CRM_WEBHOOK_SECRET", "kidoo-local-webhook-secret-24")

app = FastAPI(
    title="Kidoo Hub - Antigravity Engine (RevOps, CNPJ & CRM Vercel)",
    description="Motor RevOps com Conexão Nativa à Receita Federal (CNPJ), Google Sheets e CRM Vercel.",
    version="7.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LeadData(BaseModel):
    nome_lead: str = Field(..., description="Nome do decisor ou contato", example="Dr. Carlos Eduardo")
    empresa: Optional[str] = Field(None, description="Nome da empresa ou negócio", example="Mendonça Locações Pesadas")
    nicho: Optional[str] = Field(None, description="Nicho informado ou deduzido", example="Locação de Máquinas e Equipamentos B2B")
    faturamento: Optional[str] = Field("Não informado", description="Faturamento estimado", example="R$ 850.000/mês")
    cnpj: Optional[str] = Field(None, description="CNPJ para busca automática na Receita Federal", example="30.680.829/0001-43")
    telefone: Optional[str] = Field("5531999999999", description="WhatsApp do contato", example="5531999998888")
    email: Optional[str] = Field(None, description="E-mail do contato", example="carlos@mendonca.com.br")

class RaioXLeadResponse(BaseModel):
    nicho_profundo: str = Field(..., description="Resumo do modelo de negócios do lead.")
    dor_especifica: str = Field(..., description="O gargalo milionário que eles enfrentam.")
    solucao_arquitetada: str = Field(..., description="A solução Kidoo personalizada.")
    precificacao_sugerida: str = Field(..., description="Setup R$ X e MRR R$ Y (Value-Based Pricing).")
    gancho_vendas: str = Field(..., description="Uma pergunta C-Level para a call de 15 minutos.")
    dados_cnpj: Optional[dict] = Field(None, description="Dados oficiais da Receita Federal (se informado CNPJ)")

def extrair_faixa_faturamento(faturamento_str: str) -> str:
    fat = (faturamento_str or "").lower()
    nums = re.findall(r'\d+', fat)
    valor = int(nums[0]) if nums else 0

    if any(k in fat for k in ["milhão", "milhoes", "milhões", "1m", "2m", "enterprise"]):
        return "enterprise"
    if valor >= 400 or "500k" in fat or "600k" in fat:
        return "enterprise"
    elif valor >= 80 or "100k" in fat or "200k" in fat or "300k" in fat or "médio" in fat or "medio" in fat:
        return "medio"
    else:
        return "micro"

def gerar_analise_heuristica_c_level(lead: LeadData) -> dict:
    porte = extrair_faixa_faturamento(lead.faturamento)
    nome = lead.nome_lead.split()[0] if lead.nome_lead else "Diretor(a)"
    empresa = lead.empresa or "sua empresa"

    if porte == "enterprise":
        precificacao = "Setup R$ 12.500 e MRR R$ 4.500/mês"
        return {
            "nicho_profundo": "Operação B2B Enterprise de ciclo longo e contratos de alto valor, onde cada atrito vaza centenas de milhares de reais.",
            "dor_especifica": "Gargalo milionário de lentidão e falta de governança no atendimento inbound corporativo: executivos de conta atendendo contatos desqualificados enquanto contas Enterprise esfriam por demora no primeiro contato.",
            "solucao_arquitetada": "Kidoo Corporate Lead Routing & RevOps Engine (Triagem Técnica com IA + Round-Robin + Sincronização com CRM e ERP).",
            "precificacao_sugerida": precificacao,
            "gancho_vendas": f"{nome}, considerando que cada contrato fechado na {empresa} movimenta múltiplos 6 dígitos, quanto dinheiro a sua operação deixa na mesa todo mês por demorar mais de 10 minutos para direcionar um tomador de decisão ao executivo de conta sênior?"
        }
    elif porte == "medio":
        precificacao = "Setup R$ 5.000 e MRR R$ 1.800/mês"
        return {
            "nicho_profundo": "Negócio em forte fase de escala e tração, investindo pesado em tráfego pago, mas operando com atendimento centralizado em poucas pessoas no WhatsApp.",
            "dor_especifica": "Gargalo crítico de conversão: perda de até 30% dos leads nos picos e finais de semana, somado à alta taxa de no-show em agendamentos de alto ticket.",
            "solucao_arquitetada": "Kidoo Growth Revenue Engine (Agente Conversacional 24/7 com qualificação e quebra de objeções + Sincronização de Agendas + Régua Anti-No-Show + LP Viva de Alta Conversão).",
            "precificacao_sugerida": precificacao,
            "gancho_vendas": f"{nome}, com o volume que a {empresa} já fatura, quando um lead quente de alto ticket manda mensagem no WhatsApp sexta às 21h, quem responde ele em 5 segundos antes que ele feche com o seu principal concorrente?"
        }
    else:
        precificacao = "Setup R$ 2.500 e MRR R$ 750/mês"
        return {
            "nicho_profundo": "Operação local enxuta onde os donos ou recepcionistas acumulam atendimento ao cliente, execução operacional e cobranças.",
            "dor_especifica": "Tempo excessivo gasto digitando mensagens manuais no WhatsApp, perda de clientes fora do expediente comercial e estagnação da base antiga sem recompra.",
            "solucao_arquitetada": "Kidoo Smart Scheduling & WhatsApp AI (Agente Conversacional 24/7 + Sincronização com Google Calendar + Confirmação Automática).",
            "precificacao_sugerida": precificacao,
            "gancho_vendas": f"{nome}, hoje quantos clientes deixam de agendar na {empresa} simplesmente porque mandam mensagem à noite ou no final de semana e não encontram ninguém para responder na hora?"
        }

def gravar_direto_no_google_sheets(lead: LeadData, resultado: dict):
    """Grava o lead enriquecido diretamente na nuvem do Google Sheets sem precisar de fórmulas."""
    try:
        if not os.path.exists(CREDENCIAIS_GOOGLE_PATH):
            print(f"⚠️ Arquivo de credenciais não encontrado em {CREDENCIAIS_GOOGLE_PATH}")
            return
        
        gc = gspread.service_account(filename=CREDENCIAIS_GOOGLE_PATH)
        ss = gc.open_by_key(GOOGLE_SHEET_ID)
        ws = ss.worksheet("LEADS_INBOUND_ENRIQUECIDOS")
        
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        nova_linha = [
            data_hora,
            lead.nome_lead,
            lead.empresa or "",
            lead.nicho or "",
            lead.faturamento or "",
            resultado.get("nicho_profundo", ""),
            resultado.get("dor_especifica", ""),
            resultado.get("solucao_arquitetada", ""),
            resultado.get("precificacao_sugerida", ""),
            resultado.get("gancho_vendas", ""),
            "Pedro",
            "1 - Leads Enriquecidos",
            f"[{datetime.datetime.now().strftime('%H:%M')} - Lead Inbound]: Cadastro inicial recebido.",
            json.dumps({"faturamento": lead.faturamento, "cnpj": lead.cnpj}),
            "Indefinido",
            "",
            "",
            "FALSE",
            datetime.datetime.now().isoformat()
        ]
        ws.append_row(nova_linha)
        print(f"✅ Lead '{lead.empresa}' gravado com sucesso no Google Sheets na nuvem!")
    except Exception as e:
        print(f"⚠️ Erro ao gravar no Google Sheets: {e}")

@app.get("/", tags=["Sistema"])
async def root():
    return {
        "status": "online",
        "sistema": "Kidoo Hub - Antigravity Engine",
        "versao": "7.0.0",
        "cnpj_enrichment_ativo": True,
        "crm_kidoo_conectado": True,
        "google_sheets_conectado": True,
        "spreadsheet_id": GOOGLE_SHEET_ID
    }

@app.get("/consultar-cnpj/{cnpj}", tags=["Receita Federal & CNPJ"])
async def endpoint_consultar_cnpj(cnpj: str):
    """Consulta pública e gratuita de qualquer CNPJ na Receita Federal via BrasilAPI."""
    dados = consultar_cnpj_brasilapi(cnpj)
    if not dados.get("sucesso"):
        raise HTTPException(status_code=400, detail=dados.get("erro", "Erro ao consultar CNPJ"))
    return dados

@app.post("/enriquecer-lead", response_model=RaioXLeadResponse, tags=["RevOps & IA"])
async def processar_lead(lead: LeadData, force_heuristica: bool = Query(False, description="Forçar motor heurístico C-Level")):
    """
    Recebe o lead (com ou sem CNPJ), consulta a Receita Federal automaticamente se houver CNPJ,
    roda o diagnóstico do Gemini 1.5, grava no Google Sheets e dispara para o CRM do Erick!
    """
    cnpj_info = None
    if lead.cnpj:
        print(f"🔍 [CNPJ Detectado] Consultando Receita Federal para: {lead.cnpj}...")
        cnpj_info = consultar_cnpj_brasilapi(lead.cnpj)
        if cnpj_info.get("sucesso"):
            lead.empresa = lead.empresa or cnpj_info.get("nome_fantasia") or cnpj_info.get("razao_social")
            lead.nicho = lead.nicho or cnpj_info.get("nicho_cnae")
            if lead.faturamento in ["Não informado", None, ""]:
                lead.faturamento = cnpj_info.get("faturamento_estimado")
            print(f"🏢 Empresa identificada: {lead.empresa} ({lead.nicho}) | Porte: {lead.faturamento}")

    lead.empresa = lead.empresa or "Empresa Não Informada"
    lead.nicho = lead.nicho or "Serviços Gerais"

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or force_heuristica:
        resultado = gerar_analise_heuristica_c_level(lead)
    else:
        genai.configure(api_key=api_key)
        
        info_cnpj_str = ""
        if cnpj_info and cnpj_info.get("sucesso"):
            info_cnpj_str = f"""
DADOS OFICIAIS DA RECEITA FEDERAL:
- Razão Social: {cnpj_info.get('razao_social')}
- CNAE Oficial: {cnpj_info.get('nicho_cnae')}
- Capital Social: R$ {cnpj_info.get('capital_social'):,.2f}
- Cidade/UF: {cnpj_info.get('municipio')}/{cnpj_info.get('uf')}
- Sócios Registrados: {', '.join(cnpj_info.get('socios', []))}
"""

        prompt_inteligente = f"""
Você é o Arquiteto de Soluções e Diretor Comercial (C-Level) da Kidoo Hub.
Sua missão é atuar como um consultor hiper-personalizado e aplicar a estratégia de 'Precificação Baseada em Valor' (Value-Based Pricing). 

DADOS DO LEAD:
- Contato: {lead.nome_lead}
- Empresa: {lead.empresa}
- Nicho Informado/Deduzido: {lead.nicho}
- Faturamento Estimado: {lead.faturamento}
{info_cnpj_str}

NOSSAS TECNOLOGIAS BASE (CAIXA DE LEGO):
- Agente Conversacional (IA 24/7)
- Automação de Fluxos de Trabalho (Make.com)
- Integrações (Calendar, ERPs, CRM)
- Pix Dinâmico e Conciliação
- Motor de Reativação e Triagem B2B

INSTRUÇÕES DE ARQUITETURA E PRECIFICAÇÃO:
1. Identifique o nicho profundo e monte uma solução combinando de 2 a 4 tecnologias da nossa Caixa de Lego.
2. CALIBRE O PREÇO PELO TAMANHO DO CLIENTE. Siga estritamente estas faixas:
   - Faturamento Micro (Até R$ 50k): Setup R$ 2.000 a R$ 3.000 | MRR R$ 600 a R$ 800.
   - Faturamento Médio (R$ 100k - R$ 300k): Setup R$ 4.000 a R$ 6.000 | MRR R$ 1.500 a R$ 2.500.
   - Faturamento Enterprise/Corporate (+R$ 500k): Setup R$ 10.000 a R$ 15.000 | MRR R$ 3.500 a R$ 6.000.

FORMATO DE SAÍDA (JSON PURO OBRIGATÓRIO):
Retorne ESTRITAMENTE um objeto JSON válido:
{{
  "nicho_profundo": "Resumo do modelo de negócios do lead.",
  "dor_especifica": "O gargalo milionário que eles enfrentam.",
  "solucao_arquitetada": "A solução Kidoo personalizada.",
  "precificacao_sugerida": "Setup R$ X e MRR R$ Y",
  "gancho_vendas": "Uma pergunta C-Level para abrirmos a reunião de 15 minutos."
}}
"""
        try:
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={"response_mime_type": "application/json"}
            )
            response = model.generate_content(prompt_inteligente)
            conteudo_texto = response.text.strip()
            if conteudo_texto.startswith("```json"):
                conteudo_texto = conteudo_texto[7:]
            if conteudo_texto.startswith("```"):
                conteudo_texto = conteudo_texto[3:]
            if conteudo_texto.endswith("```"):
                conteudo_texto = conteudo_texto[:-3]
            resultado = json.loads(conteudo_texto.strip())
        except Exception as e:
            print(f"⚠️ Erro no Gemini, usando heurística: {e}")
            resultado = gerar_analise_heuristica_c_level(lead)

    if cnpj_info and cnpj_info.get("sucesso"):
        resultado["dados_cnpj"] = cnpj_info

    # 1. Gravação direta no Google Sheets
    gravar_direto_no_google_sheets(lead, resultado)

    # 2. Disparo direto para o CRM do Erick na Vercel
    try:
        disparar_lead_para_crm_kidoo(
            crm_base_url=CRM_BASE_URL,
            webhook_secret=CRM_WEBHOOK_SECRET,
            empresa=lead.empresa,
            nicho=lead.nicho,
            faturamento_str=lead.faturamento,
            contato_nome=lead.nome_lead,
            contato_telefone=lead.telefone or "5531999999999",
            contato_email=lead.email,
            nicho_profundo=resultado.get("nicho_profundo", ""),
            dor_especifica=resultado.get("dor_especifica", ""),
            solucao_arquitetada=resultado.get("solucao_arquitetada", ""),
            precificacao_sugerida=resultado.get("precificacao_sugerida", ""),
            gancho_vendas=resultado.get("gancho_vendas", "")
        )
    except Exception as e:
        print(f"⚠️ [CRM Sync Warning] Falha ao sincronizar com CRM do Erick: {e}")

    return resultado

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
