import json

# Exemplo de payload enviado pelo Make.com
lead_exemplo = {
    "nome_lead": "Dr. Fernando Silveira",
    "empresa": "Instituto Silveira Odontologia Avançada",
    "nicho": "Clínica Odontológica & Implantes / Estética",
    "faturamento": "R$ 120.000/mês"
}

# Exemplo de saída gerada pelo Arquiteto de Soluções Kidoo
resultado_esperado = {
    "maturidade_digital": "Médio-Baixo. A clínica investe em tráfego pago (Instagram/Google Ads) e possui secretária física no balcão que acumula atendimento telefônico e WhatsApp, gerando gargalo nos picos e resposta nula após as 18h e finais de semana.",
    "gargalos_operacionais": "1) Vazamento de leads de alto ticket fora do horário comercial (perda de orçamentos para concorrentes que respondem na hora). 2) Alta taxa de no-show (15% a 25%) por ausência de uma régua automatizada de confirmação multicanal no WhatsApp.",
    "fit_kidoo": "Pacote Growth (Setup: R$ 4.800 + MRR: R$ 1.850/mês). Motivo: Com faturamento de R$ 120k/mês e alto ticket em implantes, eles precisam não apenas do Agente de IA para responder em 5s e zerar no-show, mas de integração direta com CRM para o SDR virtual qualificar o procedimento desejado antes de agendar com o Dr. Fernando.",
    "gancho_vendas": "Dr. Fernando, quando um paciente de implante manda mensagem no seu WhatsApp sexta-feira às 21h procurando orçamento, quem está respondendo ele em menos de 2 minutos para garantir que ele não agende com a clínica vizinha no sábado de manhã?"
}

print("=== EXEMPLO DE SAÍDA DO ARQUITETO DE SOLUÇÕES KIDOO HUB (JSON PURO) ===")
print(json.dumps(resultado_esperado, indent=2, ensure_ascii=False))
