# -*- coding: utf-8 -*-
import json
from main import LeadData, gerar_analise_heuristica_c_level

casos_de_teste = [
    LeadData(
        nome_lead="Marcelo 'Barba' Ribeiro",
        empresa="Barbearia Dom Pedro Vintage",
        nicho="Barbearia Premium e Cuidados Masculinos",
        faturamento="R$ 35.000/mês (Micro)"
    ),
    LeadData(
        nome_lead="Dra. Juliana Mendes",
        empresa="Clínica Estética & Dermatologia Savassi",
        nicho="Estética Médica e Harmonização Facial",
        faturamento="R$ 180.000/mês (Médio)"
    ),
    LeadData(
        nome_lead="Carlos Mendonça",
        empresa="Mendonça Locação de Guindastes e Máquinas Pesadas",
        nicho="Locação B2B de Equipamentos Industriais",
        faturamento="R$ 850.000/mês (Enterprise)"
    )
]

print("========================================================================================")
print("TESTE ARQUITETO C-LEVEL KIDOO HUB — PRECIFICAÇÃO BASEADA EM VALOR (VALUE-BASED PRICING)")
print("========================================================================================\n")

for i, lead in enumerate(casos_de_teste, 1):
    print(f"[{i}] ANALISANDO LEAD: {lead.empresa} ({lead.nicho})")
    print(f"Decisor: {lead.nome_lead} | Faturamento: {lead.faturamento}")
    raio_x = gerar_analise_heuristica_c_level(lead)
    print("RESPOSTA JSON PURO:")
    print(json.dumps(raio_x, indent=2, ensure_ascii=False))
    print("-" * 80 + "\n")
