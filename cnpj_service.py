# -*- coding: utf-8 -*-
"""
MÓDULO DE CONSULTA E ENRIQUECIMENTO AUTOMÁTICO DE CNPJ (KIDOO HUB)
Conexão direta com a Receita Federal via BrasilAPI (Pública, rápida e gratuita).
"""

import re
import urllib.request
import ssl
import json

ctx = ssl._create_unverified_context()

def limpar_cnpj(cnpj: str) -> str:
    """Remove caracteres especiais deixando apenas os 14 dígitos numéricos."""
    if not cnpj:
        return ""
    return re.sub(r'\D', '', str(cnpj))

def consultar_cnpj_brasilapi(cnpj_raw: str) -> dict:
    """
    Consulta o CNPJ na BrasilAPI e devolve um resumo corporativo pronto para a IA.
    """
    cnpj = limpar_cnpj(cnpj_raw)
    if len(cnpj) != 14:
        return {"sucesso": False, "erro": "CNPJ deve conter 14 dígitos"}

    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (KidooHub-RevOps)"})

    try:
        with urllib.request.urlopen(req, timeout=6, context=ctx) as r:
            dados = json.loads(r.read().decode("utf-8"))
            
            razao_social = dados.get("razao_social", "")
            nome_fantasia = dados.get("nome_fantasia") or razao_social
            cnae_descricao = dados.get("cnae_fiscal_descricao") or "Serviços B2B"
            capital_social = float(dados.get("capital_social") or 0.0)
            porte = dados.get("porte", "DEMAIS")
            
            # Quadro Societário
            socios = [s.get("nome_socio") for s in dados.get("qsa", []) if s.get("nome_socio")]
            
            # Estimativa de Faturamento com base em Capital Social e Porte
            if capital_social >= 500000 or porte == "DEMAIS":
                faixa_faturamento = "R$ 500.000+/mês (Enterprise)"
            elif capital_social >= 100000 or porte == "EMPRESA DE PEQUENO PORTE":
                faixa_faturamento = "R$ 100.000 a R$ 300.000/mês (Médio)"
            else:
                faixa_faturamento = "Até R$ 50.000/mês (Micro)"

            return {
                "sucesso": True,
                "cnpj": cnpj,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia,
                "nicho_cnae": cnae_descricao,
                "capital_social": capital_social,
                "porte": porte,
                "faturamento_estimado": faixa_faturamento,
                "socios": socios[:4],
                "municipio": dados.get("municipio", ""),
                "uf": dados.get("uf", "")
            }
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

if __name__ == "__main__":
    # Teste rápido
    res = consultar_cnpj_brasilapi("30680829000143")
    print("Resultado Teste:", json.dumps(res, indent=2, ensure_ascii=False))
