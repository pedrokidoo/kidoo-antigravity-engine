# 🏛️ KIDOO HUB — MANUAL MESTRE DE OPERAÇÕES, REVOPS E ARQUITETURA C-LEVEL
**Documento Oficial de Engenharia, Precificação e Inteligência Comercial**  
**Versão:** 5.0 (Definitiva / Master) | **Data:** 13 de Outubro de 2026  
**Sócios Fundadores:** Pedro (CEO & Tecnologia), Arthur (Head de Aquisição), Erick (Head de Infraestrutura)

---

## 📌 SUMÁRIO EXECUTIVO

Este documento encapsula a totalidade do ecossistema da **Kidoo Hub**: nosso modelo societário, divisão de lucros, esteira de tecnologias base (Caixa de Lego), estratégia comercial C-Level de **Precificação Baseada em Valor (Value-Based Pricing)**, o microserviço **Antigravity Engine**, a integração completa com **Make.com**, o **Google Sheets com Sincronização em Tempo Real (F5)** e o playbook de condução de calls de 15 minutos.

---

## 1. ESTRUTURA SOCIETÁRIA E REGRAS FINANCEIRAS

A Kidoo Hub atua como Integradora de Tecnologia B2B, unindo Infraestrutura Web, Aquisição de Tráfego e Automações Cognitivas com Inteligência Artificial para gerar previsibilidade, retenção e receita recorrente (MRR).

### 1.1 Divisão de Frentes
* **Pedro (CEO & Tecnologia):** Desenvolvimento dos Agentes Cognitivos de IA (WhatsApp 24/7, agendamento no Google Calendar/Booksy, réguas anti-no-show, conciliação de Pix Dinâmico, integração com impressoras térmicas ESC/POS, triagem técnica B2B Round-Robin, webhooks e orquestração de APIs).
* **Arthur (Head de Aquisição):** Gestão de Tráfego Pago local e estratégico, campanhas no Meta Ads e Google Ads, esteiras de remarketing, rastreamento via UTMIFY e geração contínua de demanda.
* **Erick (Head de Infraestrutura & Produto):** Landing Pages Vivas de Alta Conversão ("Pistas de Pouso"), Sites Institucionais Multipáginas com SEO de base e Bio Executiva / Linktree próprio rastreável.

### 1.2 Regras de Divisão Financeira
* **Setups (Projetos Pontuais - Regra 60/40):**
  * **60%** do valor total do setup é repassado diretamente ao sócio executor do serviço.
  * **40%** é destinado ao caixa compartilhado da Kidoo Hub (distribuído igualmente entre os três sócios).
* **Mensalidades Recorrentes (MRR):**
  * **Dedução de Custos Diretos:** Abatimento prioritário de custos operacionais (Make.com, API Oficial WhatsApp, tokens de IA OpenAI/Gemini e servidores).
  * **Distribuição do Lucro Líquido:** O saldo remanescente é distribuído igualmente na proporção de **33,33% para cada sócio**.
* **Estratégia Cavalo de Troia (Web com IA Acoplada):** Venda da Landing Page (R$ 1.200) já conectada nativamente ao ecossistema de WhatsApp com IA da Kidoo, transformando vendas pontuais em contratos de MRR contínuo.

---

## 2. A CAIXA DE LEGO KIDOO (NOSSAS TECNOLOGIAS BASE)

Não oferecemos pacotes engessados. Como Arquiteto de Soluções e Diretor Comercial C-Level, analisamos a operação do lead, identificamos o nicho profundo e montamos uma **Solução Personalizada** combinando de 2 a 4 tecnologias da nossa Caixa de Lego:

1. **Agente Conversacional (IA 24/7):** Atendimento humanizado e contextual via WhatsApp e Direct, qualificação e fechamento em menos de 5 segundos.
2. **Automação de Fluxos de Trabalho (Make.com):** Webhooks, processamento em lote, gatilhos de CRM e orquestração de APIs.
3. **Sincronização de Agendas (Calendar, ERPs, CRM):** Sincronização em tempo real com Google Calendar, Booksy, RD Station, HubSpot, Pipedrive e ERPs.
4. **Pix Dinâmico e Conciliação:** Geração instantânea de QR Code com conciliação automática via webhook bancário e impressão térmica remota (ESC/POS).
5. **Motor de Reativação e Triagem B2B:** Higienização de bases antigas (> 300 contatos) e algoritmo de roteamento Round-Robin para consultores sêniores.
6. **Infraestrutura Web:** Landing pages ultrarrápidas de alta conversão e sites multipáginas.

---

## 3. FILOSOFIA C-LEVEL: PRECIFICAÇÃO BASEADA EM VALOR (VALUE-BASED PRICING)

Cobramos pelo tamanho do cliente e pelo impacto direto na última linha do balanço (EBITDA, redução de custo de folha e governança).

> ⚠️ **Regra Comercial Inegociável:**  
> Em vendas B2B corporativas, cobrar barato de uma empresa grande passa percepção imediata de fragilidade e baixa qualidade. Calibramos rigorosamente por porte:

| Porte do Lead | Faixa de Faturamento Mensal | Setup Sugerido | MRR Mensal Sugerido | Abordagem Comercial C-Level |
| :--- | :--- | :--- | :--- | :--- |
| **Micro** | Até **R$ 50.000/mês** | **R$ 2.000 a R$ 3.000** | **R$ 600 a R$ 800/mês** | Venda alívio operacional, economia de tempo e captura de clientes fora de hora. |
| **Médio** | **R$ 100.000 a R$ 300.000/mês** | **R$ 4.000 a R$ 6.000** | **R$ 1.500 a R$ 2.500/mês** | Venda aceleração de receita, qualificação com lead scoring e esteira de vendas integrada. |
| **Enterprise / Corporate** | Acima de **R$ 500.000/mês** | **R$ 10.000 a R$ 15.000** | **R$ 3.500 a R$ 6.000/mês** | Venda governança, exclusividade, redução de churn e impacto direto no EBITDA da empresa. |

---

## 4. O MOTOR TÉCNICO: ANTIGRAVITY ENGINE

Microserviço em FastAPI desenvolvido para receber webhooks do Make.com, processar o lead via **Google Gemini 1.5 Flash** e devolver o Raio-X em **JSON Puro** estruturado.

### 4.1 Prompt do Arquiteto C-Level Integrado na API:
```python
prompt_inteligente = f"""
Você é o Arquiteto de Soluções e Diretor Comercial (C-Level) da Kidoo Hub.
Sua missão é atuar como um consultor hiper-personalizado e aplicar a estratégia de 'Precificação Baseada em Valor' (Value-Based Pricing). 

DADOS DO LEAD:
- Contato: {lead.nome_lead}
- Empresa: {lead.empresa}
- Nicho Informado/Deduzido: {lead.nicho}
- Faturamento Estimado: {lead.faturamento}

NOSSAS TECNOLOGIAS BASE:
- Agente Conversacional (IA 24/7)
- Automação de Fluxos de Trabalho (Make.com)
- Integrações (Calendar, ERPs, CRM)
- Pix Dinâmico e Conciliação
- Motor de Reativação e Triagem B2B

INSTRUÇÕES DE ARQUITETURA E PRECIFICAÇÃO:
1. Identifique o nicho e monte uma solução combinando nossas tecnologias base.
2. CALIBRE O PREÇO PELO TAMANHO DO CLIENTE. Em B2B, preço baixo para empresa grande passa percepção de fragilidade e baixa qualidade. Siga esta regra de MRR e Setup:
   - Faturamento Micro (Até R$ 50k): Setup R$ 2.000 a R$ 3.000 | MRR R$ 600 a R$ 800.
   - Faturamento Médio (R$ 100k - R$ 300k): Setup R$ 4.000 a R$ 6.000 | MRR R$ 1.500 a R$ 2.500.
   - Faturamento Enterprise/Corporate (+R$ 500k): Setup R$ 10.000 a R$ 15.000 | MRR R$ 3.500 a R$ 6.000. (Venda governança, exclusividade e impacto direto na última linha do balanço).

FORMATO DE SAÍDA (JSON PURO OBRIGATÓRIO):
Retorne ESTRITAMENTE um objeto JSON válido, sem crases markdown:
{{
  "nicho_profundo": "Resumo do modelo de negócios do lead.",
  "dor_especifica": "O gargalo milionário que eles enfrentam.",
  "solucao_arquitetada": "A solução Kidoo (Ex: Kidoo Corporate Routing).",
  "precificacao_sugerida": "Setup R$ X e MRR R$ Y (exatamente dentro das regras de faturamento acima)",
  "gancho_vendas": "Uma pergunta C-Level para abrirmos a reunião de 15 minutos."
}}
"""
```

### 4.2 Contrato de Saída (JSON Puro Estruturado — 5 Chaves):
```json
{
  "nicho_profundo": "Operação B2B Enterprise de ciclo longo e contratos de alto valor, onde cada ponto de atrito entre marketing e vendas vaza centenas de milhares de reais.",
  "dor_especifica": "Gargalo milionário de lentidão e falta de governança no atendimento inbound: executivos de conta atendendo contatos desqualificados enquanto contas Enterprise esfriam por demora no primeiro contato.",
  "solucao_arquitetada": "Kidoo Corporate Lead Routing & RevOps Engine (Triagem Técnica com IA + Algoritmo Round-Robin para Diretores/Closers + Sincronização Bidirecional com CRM corporativo e ERP).",
  "precificacao_sugerida": "Setup R$ 12.500 e MRR R$ 4.500/mês",
  "gancho_vendas": "Carlos, considerando que cada contrato fechado na Mendonça Locação movimenta múltiplos 6 dígitos, quanto dinheiro a sua operação deixa na mesa todo mês por demorar mais de 10 minutos para direcionar um tomador de decisão ao executivo de conta sênior?"
}
```

---

## 5. COMO FUNCIONA A ATUALIZAÇÃO NO GOOGLE SHEETS COM "F5" (LIVE-SYNC)

Você perguntou: **"Tem como essas mudanças acontecerem automaticamente no Google Sheets, só dando um F5 e atualiza lá?"**  
**SIM! Implementamos isso através de duas maneiras nativas e infalíveis:**

### Método 1: A Fórmula Mágica `=IMPORTDATA` (Mais Fácil do Mundo)
Na sua API do Antigravity Engine, criamos o endpoint:
`GET /sheets/leads-csv`

Como usar:
1. Abra sua planilha do Google Sheets.
2. Em uma aba nova (ou na célula **A1**), cole simplesmente:
   ```excel
   =IMPORTDATA("https://sua-url-api/sheets/leads-csv")
   ```
3. **Como funciona:** Sempre que você der **F5** no navegador ou reabrir a planilha, o Google Sheets faz uma requisição ao vivo para o seu servidor, pega todos os leads novos analisados e repopula todas as colunas automaticamente, em tempo real!

### Método 2: Via Gatilho `onOpen()` do Google Apps Script
No arquivo [`codigo_apps_script_kidoo.js`](file:///C:/Users/pedro/.gemini/antigravity-ide/scratch/kidoo-antigravity-engine/codigo_apps_script_kidoo.js), configuramos a função `onOpen()`. Sempre que a planilha é aberta ou atualizada com F5, ela executa a sincronização e adiciona o menu **🚀 Kidoo Hub RevOps > Sincronizar Agora**.

---

## 6. INTEGRAÇÃO NO MAKE.COM (CENÁRIO EM 4 MÓDULOS)

O arquivo [`blueprint_make_kidoo.json`](file:///C:/Users/pedro/OneDrive/Desktop/blueprint_make_kidoo.json) pronto na sua Área de Trabalho implementa o seguinte fluxo:
1. **Módulo 1 (Custom Webhook):** Recebe o lead da Landing Page ou Meta Ads (`nome`, `empresa`, `nicho`, `faturamento`).
2. **Módulo 2 (HTTP - Make a request):** Envia `POST /enriquecer-lead` para o Antigravity Engine com `Parse response: Yes`.
3. **Módulo 3 (Google Sheets - Add a Row):** Grava a linha na aba `LEADS_INBOUND_ENRIQUECIDOS`.
4. **Módulo 4 (WhatsApp / Evolution API):** Notifica os sócios no WhatsApp com a dor específica e a pergunta de abertura C-Level.

---

## 7. PASSO A PASSO DEFINITIVO PARA "FAZER ACONTECER"

### Passo 1: Iniciar o Servidor Antigravity
No terminal PowerShell:
```powershell
cd C:\Users\pedro\.gemini\antigravity-ide\scratch\kidoo-antigravity-engine
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Passo 2: Expor com URL Pública Gratuita
Em outra aba do terminal:
```powershell
npx localtunnel --port 8000
# Ou: ngrok http 8000
```
Copie a URL gerada (ex: `https://kidoo-revops.loca.lt`).

### Passo 3: Importar a Planilha no Google Sheets
1. Acesse [sheets.new](https://sheets.new).
2. Vá em **Arquivo > Importar > Fazer upload**.
3. Selecione o arquivo `PLANILHA_KIDOO_REVOPS_INBOUND.xlsx` da sua Área de Trabalho.
4. Escolha **Substituir planilha atual**.
5. *(Opcional para Live-Sync automático no F5):* Na célula A1 de uma aba auxiliar, digite: `=IMPORTDATA("https://kidoo-revops.loca.lt/sheets/leads-csv")`.

### Passo 4: Importar o Cenário no Make.com
1. No [Make.com](https://make.com), crie um novo cenário.
2. Clique no menu de **três pontinhos (...)** na barra inferior e selecione **Import Blueprint**.
3. Selecione o arquivo `blueprint_make_kidoo.json` da sua Área de Trabalho.
4. No Módulo 2 (HTTP), cole a URL do seu túnel.
5. No Módulo 3 (Google Sheets), selecione sua planilha.
6. Clique em **Save** e ative para **ON**.

### Passo 5: A Call de Fechamento C-Level de 15 Minutos
Assim que o alerta apitar no WhatsApp:
1. Veja na planilha o porte e a **Precificação Sugerida** calibrada.
2. Abra a reunião diretamente com a pergunta do **Gancho de Vendas C-Level**, sem papo genérico de vendedor.
3. Apresente a arquitetura exclusiva da Kidoo e feche a proposta ancorada no valor milionário gerado.
