# -*- coding: utf-8 -*-
"""
TESTE COMPLETO: ENRIQUECIMENTO AUTOMÁTICO DE LEAD POR CNPJ
"""
import sys
import asyncio

sys.stdout.reconfigure(encoding='utf-8')
from main import processar_lead, LeadData

async def rodar_teste():
    print("\n--- INICIANDO TESTE COM CNPJ (SEM DIGITAR NOME DA EMPRESA NEM NICHO) ---")
    lead_cnpj = LeadData(
        nome_lead="Arthur Valadão",
        cnpj="30.680.829/0001-43",
        telefone="5531995870862",
        email="arthur@kidoohub.com.br"
    )
    
    res = await processar_lead(lead_cnpj, force_heuristica=True)
    print("\n🎉 RESULTADO DO RAIO-X OBTIDO AUTOMATICAMENTE:")
    print("Empresa:", lead_cnpj.empresa)
    print("Nicho (CNAE):", lead_cnpj.nicho)
    print("Faturamento Estimado:", lead_cnpj.faturamento)
    print("Nicho Profundo:", res.get("nicho_profundo"))
    print("Dor Específica:", res.get("dor_especifica"))
    print("Solução Kidoo:", res.get("solucao_arquitetada"))
    print("Precificação Sugerida:", res.get("precificacao_sugerida"))
    print("Gancho C-Level:", res.get("gancho_vendas"))

if __name__ == "__main__":
    asyncio.run(rodar_teste())
