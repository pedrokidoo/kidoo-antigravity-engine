# 🚀 Kidoo Hub - Antigravity Engine (RevOps & Lead Intelligence)

Microserviço FastAPI desenvolvido para receber webhooks do **Make.com**, realizar engenharia reversa operacional do lead inbound via **Google Gemini** e devolver um Raio-X estratégico completo em formato **JSON Puro**.

---

## 📦 Estrutura do Projeto

- `main.py`: Aplicação FastAPI com endpoint `/enriquecer-lead`, tratamento de exceções e CORS.
- `portfolio.py`: Tabela oficial de pacotes, escopo, Setup e MRR da Kidoo Hub.
- `teste_lead_exemplo.py`: Demonstração da estrutura e do JSON esperado.
- `.env`: Arquivo com a chave `GEMINI_API_KEY`.
- `requirements.txt`: Dependências necessárias (`fastapi`, `uvicorn`, `google-generativeai`, `pydantic`, `python-dotenv`).

---

## ⚡ Instalação e Execução

### 1. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar a chave da API
Crie um arquivo `.env` na raiz do diretório com sua chave:
```env
GEMINI_API_KEY=sua_chave_do_google_ai_studio
```

### 3. Iniciar o servidor
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔗 Integração com Make.com

1. No Make.com, adicione um módulo **HTTP - Make a request**.
2. **URL**: `https://seu-servidor-ou-ngrok/enriquecer-lead`
3. **Method**: `POST`
4. **Headers**: `Content-Type: application/json`
5. **Body Type**: `Raw` (JSON)
6. **Request content**:
```json
{
  "nome_lead": "{{1.nome}}",
  "empresa": "{{1.empresa}}",
  "nicho": "{{1.nicho}}",
  "faturamento": "{{1.faturamento}}"
}
```

O endpoint responderá imediatamente com o JSON limpo contendo:
- `maturidade_digital`
- `gargalos_operacionais`
- `fit_kidoo`
- `gancho_vendas`
