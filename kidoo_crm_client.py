# -*- coding: utf-8 -*-
"""
KIDOO HUB — CLIENTE OFICIAL DE INTEGRAÇÃO COM O CRM DO ERICK
Segue 100% a validação do Zod schema: antigravityWebhook (@kidoo/shared)
Endpoint: POST /api/v1/webhooks/antigravity
Header: x-webhook-secret
"""

import os
import re
import uuid
import datetime
import requests

def extrair_numeros(texto: str) -> float:
    """Extrai o primeiro valor numérico de uma string (ex: 'Setup R$ 5.000' -> 5000.0)"""
    if not texto:
        return 0.0
    limpo = re.sub(r'[^\d,.]', '', str(texto)).replace('.', '').replace(',', '.')
    try:
        return float(limpo)
    except Exception:
        return 0.0

def extrair_setup_e_mrr(precificacao_str: str) -> tuple[float, float]:
    """Extrai os valores numéricos de Setup e MRR a partir da string sugerida."""
    texto = precificacao_str or ""
    setup = 3000.0
    mrr = 800.0
    
    m_setup = re.search(r'Setup\s*(?:R\$\s*)?([\d.,]+)', texto, re.IGNORECASE)
    if m_setup:
        setup = extrair_numeros(m_setup.group(1))
        
    m_mrr = re.search(r'MRR\s*(?:R\$\s*)?([\d.,]+)', texto, re.IGNORECASE)
    if m_mrr:
        mrr = extrair_numeros(m_mrr.group(1))
        
    return setup, mrr

def disparar_lead_para_crm_kidoo(
    crm_base_url: str,
    webhook_secret: str,
    empresa: str,
    nicho: str,
    faturamento_str: str,
    contato_nome: str,
    contato_telefone: str = "5531999999999",
    contato_email: str = None,
    nicho_profundo: str = "",
    dor_especifica: str = "",
    solucao_arquitetada: str = "",
    precificacao_sugerida: str = "",
    gancho_vendas: str = ""
) -> dict:
    """
    Dispara o lead enriquecido no formato exato que o backend do Erick valida via Zod.
    """
    endpoint = f"{crm_base_url.rstrip('/')}/api/v1/webhooks/antigravity"
    event_id = f"ag-{uuid.uuid4().hex[:12]}"
    agora_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    faturamento_num = extrair_numeros(faturamento_str) or 100000.0
    setup_num, mrr_num = extrair_setup_e_mrr(precificacao_sugerida)

    headers = {
        "x-webhook-secret": webhook_secret,
        "Content-Type": "application/json"
    }

    # Payload estritamente validado pelo antigravityWebhook do Erick
    payload = {
        "event_id": event_id,
        "event_type": "lead.enriched",
        "company": {
            "name": empresa,
            "industry": nicho,
            "estimated_monthly_revenue": faturamento_num
        },
        "contact": {
            "name": contato_nome,
            "phone": contato_telefone,
            "email": contato_email
        },
        "diagnostic": {
            "deep_niche": nicho_profundo,
            "specific_pain": dor_especifica,
            "proposed_solution": solucao_arquitetada,
            "suggested_setup": setup_num,
            "suggested_mrr": mrr_num,
            "opening_hook": gancho_vendas,
            "generated_at": agora_iso
        },
        "source": "antigravity"
    }

    print(f"\n🚀 [CRM Sync] Enviando lead '{empresa}' para: {endpoint}")
    print(f"📦 Event ID: {event_id} | Setup: R$ {setup_num:,.2f} | MRR: R$ {mrr_num:,.2f}")

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=12)
        print(f"📡 Status Code retornado: {response.status_code}")
        try:
            resp_body = response.json()
        except Exception:
            resp_body = response.text
        print(f"📄 Resposta do CRM: {resp_body}")
        return {"status_code": response.status_code, "resposta": resp_body}
    except Exception as e:
        print(f"❌ Erro de conexão com o CRM do Erick: {e}")
        return {"status_code": 500, "erro": str(e)}

if __name__ == "__main__":
    print("Módulo de integração alinhado com o Zod schema de @kidoo/shared!")
