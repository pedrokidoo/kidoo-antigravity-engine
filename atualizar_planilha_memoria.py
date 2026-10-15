# -*- coding: utf-8 -*-
import sys
import gspread

sys.stdout.reconfigure(encoding='utf-8')

CREDENCIAIS = r"C:\Users\pedro\OneDrive\Desktop\kidoo\Json kidoo\kidoo-hub-492476e23d24.json"
SPREADSHEET_ID = "1PRprGhbag7oxvoIG_zrDjXQSupadKIgBguMinkdHzrg"

COLUNAS_NOVAS = [
    "HISTORICO_CHAT",
    "MEMORIA_IA_JSON",
    "PERFIL_COMPORTAMENTAL",
    "LINK_MEET",
    "DATA_HORA_CALL",
    "MODO_HUMANO",
    "ULTIMA_INTERACAO_TIMESTAMP"
]

def atualizar():
    gc = gspread.service_account(filename=CREDENCIAIS)
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet("LEADS_INBOUND_ENRIQUECIDOS")
    
    # Limpar qualquer lixo que tenha caído na linha 1
    # Linha 1 deve ter apenas a célula A1
    linha1 = ws.row_values(1)
    if len(linha1) > 1:
        for c in range(2, len(linha1) + 1):
            ws.update_cell(1, c, "")
            
    # Linha 2 é onde estão os cabeçalhos das colunas
    headers = ws.row_values(2)
    print("Cabeçalhos atuais na Linha 2 (Total: %d):" % len(headers))
    for i, h in enumerate(headers, 1):
        print(f"  [{i:02d}] {h}")
        
    start_col = len(headers) + 1
    adicionadas = []
    for i, col in enumerate(COLUNAS_NOVAS):
        if col not in headers:
            col_idx = start_col + len(adicionadas)
            ws.update_cell(2, col_idx, col)
            adicionadas.append(col)
            print(f"➕ Adicionada coluna [{col_idx:02d}]: {col}")
            
    headers_finais = ws.row_values(2)
    print(f"\n✅ Concluído! Total de colunas na Linha 2: {len(headers_finais)}")
    for i, h in enumerate(headers_finais, 1):
        print(f"  [{i:02d}] {h}")

if __name__ == "__main__":
    atualizar()
