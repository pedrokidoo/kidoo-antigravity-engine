# 🚀 KIDOO HUB — MANUAL EXECUTIVO DE OPERAÇÕES, REVOPS E PRECIFICAÇÃO C-LEVEL (VALUE-BASED PRICING)
**Data de Emissão:** 13 de Outubro de 2026  
**Liderança:** Pedro (CEO & Tecnologia), Arthur (Aquisição & Tráfego), Erick (Infraestrutura & Produto)  
**Objetivo:** Guia Mestre de Arquitetura Consultiva C-Level, Precificação Baseada em Valor por Porte, Integração Make.com, Google Sheets e Fechamento Comercial em 15 minutos.

---

## 1. VISÃO GERAL DO MODELO DE NEGÓCIO E SOCIEDADE

A **Kidoo Hub** atua como Integradora de Tecnologia B2B, unindo Infraestrutura Web de Alta Performance, Aquisição de Tráfego Pago e Automações Cognitivas com Inteligência Artificial para gerar previsibilidade, retenção e receita recorrente (MRR).

### 1.1 Papéis e Frentes dos Sócios
* **Pedro (CEO & Tecnologia):** Desenvolvimento e implantação de Agentes Cognitivos de IA (WhatsApp 24/7, agendamento no Google Calendar/Booksy, réguas anti-no-show, conciliação de Pix Dinâmico, integração com impressoras térmicas ESC/POS, triagem técnica B2B Round-Robin e fluxos Make.com).
* **Arthur (Head de Aquisição):** Tráfego Pago local e estratégico, Meta Ads, Google Ads, esteiras de remarketing, rastreamento via UTMIFY e geração contínua de demanda.
* **Erick (Head de Infraestrutura & Produto):** Landing Pages Vivas de Alta Conversão ("Pistas de Pouso"), Sites Institucionais Multipáginas com SEO de base e Bio Executiva / Linktree próprio rastreável.

### 1.2 Regras Financeiras e Divisão da Sociedade
* **Setups (Projetos Pontuais - Regra 60/40):** 
  * **60%** do valor total do setup é repassado diretamente ao sócio executor do serviço.
  * **40%** é destinado ao caixa compartilhado da Kidoo Hub (distribuído igualmente entre os três sócios).
* **Mensalidades Recorrentes (MRR):**
  * **Dedução de Custos Diretos:** Abatimento prioritário de custos operacionais (Make.com, API Oficial WhatsApp, tokens de IA OpenAI/Gemini e servidores).
  * **Distribuição do Lucro Líquido:** O saldo remanescente é distribuído igualmente na proporção de **33,33% para cada sócio**.
* **Estratégia Cavalo de Troia (Web com IA Acoplada):** Venda da Landing Page (R$ 1.200) conectada nativamente ao ecossistema de WhatsApp com IA da Kidoo, convertendo vendas pontuais em contratos de MRR contínuo.

---

## 2. FILOSOFIA C-LEVEL: PRECIFICAÇÃO BASEADA EM VALOR (VALUE-BASED PRICING)

Abandonamos qualquer tabela de preços fixa ou pacotes engessados. Como Arquiteto de Soluções e Diretor Comercial (C-Level), nossa missão é **calibrar o preço pelo tamanho e capacidade financeira do lead**.

> ⚠️ **Princípio Comercial Inegociável:**  
> Em vendas B2B corporativas, cobrar barato de uma empresa grande passa percepção imediata de amadorismo, fragilidade estrutural e baixa qualidade. Para grandes contas, cobramos pelo impacto direto na última linha do balanço (governança, redução de custo de folha e blindagem de SLAs).

### 2.1 Matriz Oficial de Calibração de Preço

| Porte do Lead | Faixa de Faturamento Mensal | Setup Sugerido | MRR Mensal Sugerido | Abordagem Comercial C-Level |
| :--- | :--- | :--- | :--- | :--- |
| **Micro** | Até **R$ 50.000/mês** | **R$ 2.000 a R$ 3.000** | **R$ 600 a R$ 800/mês** | Venda alívio operacional, economia de tempo e captura de clientes fora do expediente. |
| **Médio** | **R$ 100.000 a R$ 300.000/mês** | **R$ 4.000 a R$ 6.000** | **R$ 1.500 a R$ 2.500/mês** | Venda aceleração de receita, qualificação com lead scoring e esteira de vendas integrada. |
| **Enterprise / Corporate** | Acima de **R$ 500.000/mês** | **R$ 10.000 a R$ 15.000** | **R$ 3.500 a R$ 6.000/mês** | Venda governança, exclusividade, redução de churn e impacto direto no EBITDA da empresa. |

---

## 3. NOSSAS TECNOLOGIAS BASE (SUA CAIXA DE LEGO)

Combinamos de 2 a 4 tecnologias abaixo para montar a arquitetura exclusiva de cada lead:
1. **Agente Conversacional (IA 24/7):** Atendimento humanizado e contextual via WhatsApp e Direct, qualificação e fechamento em menos de 5 segundos.
2. **Automação de Fluxos de Trabalho (Make.com):** Webhooks, processamento em lote, gatilhos de CRM e orquestração de APIs.
3. **Integrações (Calendar, ERPs, CRM):** Sincronização em tempo real com Google Calendar, RD Station, HubSpot, Pipedrive e ERPs locais.
4. **Pix Dinâmico e Conciliação:** Geração instantânea de QR Code com conciliação automática via webhook bancário e impressão térmica remota (ESC/POS).
5. **Motor de Reativação e Triagem B2B:** Higienização de bases antigas (> 300 contatos) e algoritmo de roteamento Round-Robin para consultores sêniores.

---

## 4. O MOTOR TÉCNICO (ANTIGRAVITY ENGINE)

Microserviço FastAPI construído para receber webhooks do Make.com, analisar o lead via **Google Gemini 1.5 Flash** e devolver uma resposta em **JSON Puro** estruturado.

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

### 4.2 Exemplos Reais de Saída por Faixa de Faturamento:

#### Exemplo 1: Lead Enterprise (Faturamento R$ 850k/mês)
```json
{
  "nicho_profundo": "Operação B2B Enterprise de ciclo longo e contratos de alto valor, onde cada ponto de atrito entre marketing e vendas vaza centenas de milhares de reais.",
  "dor_especifica": "Gargalo milionário de lentidão e falta de governança no atendimento inbound: executivos de conta atendendo contatos desqualificados enquanto contas Enterprise esfriam por demora no primeiro contato.",
  "solucao_arquitetada": "Kidoo Corporate Lead Routing & RevOps Engine (Triagem Técnica com IA + Algoritmo Round-Robin para Diretores/Closers + Sincronização Bidirecional com CRM corporativo e ERP).",
  "precificacao_sugerida": "Setup R$ 12.500 e MRR R$ 4.500/mês",
  "gancho_vendas": "Carlos, considerando que cada contrato fechado na Mendonça Locação movimenta múltiplos 6 dígitos, quanto dinheiro a sua operação deixa na mesa todo mês por demorar mais de 10 minutos para direcionar um tomador de decisão ao executivo de conta sênior?"
}
```

#### Exemplo 2: Lead Médio (Faturamento R$ 180k/mês)
```json
{
  "nicho_profundo": "Negócio em forte fase de escala e tração, investindo pesado em tráfego pago, mas operando com atendimento centralizado em poucas pessoas no WhatsApp.",
  "dor_especifica": "Gargalo crítico de conversão: perda de até 30% dos leads nos picos e finais de semana, somado à alta taxa de no-show em agendamentos de procedimentos de alto ticket.",
  "solucao_arquitetada": "Kidoo Growth Revenue Engine (Agente Conversacional 24/7 com qualificação e quebra de objeções + Sincronização de Agendas + Régua Ativa Anti-No-Show + LP Viva de Alta Conversão).",
  "precificacao_sugerida": "Setup R$ 5.000 e MRR R$ 1.800/mês",
  "gancho_vendas": "Dra. Juliana, com o volume que a clínica já fatura, quando um lead quente de alto ticket manda mensagem no WhatsApp sexta às 21h, quem responde ele em 5 segundos antes que ele feche com o seu principal concorrente?"
}
```

#### Exemplo 3: Lead Micro (Faturamento R$ 35k/mês)
```json
{
  "nicho_profundo": "Operação local enxuta onde os donos ou recepcionistas acumulam atendimento ao cliente, execução operacional e cobranças.",
  "dor_especifica": "Tempo excessivo gasto digitando mensagens manuais no WhatsApp, perda de clientes fora do expediente comercial e estagnação da base antiga sem recompra.",
  "solucao_arquitetada": "Kidoo Smart Scheduling & WhatsApp AI (Agente Conversacional 24/7 + Sincronização com Google Calendar + Confirmação Automática de Horários).",
  "precificacao_sugerida": "Setup R$ 2.500 e MRR R$ 750/mês",
  "gancho_vendas": "Marcelo, hoje quantos clientes deixam de agendar na Dom Pedro simplesmente porque mandam mensagem à noite ou no final de semana e não encontram ninguém para responder na hora?"
}
```

---

## 5. ESTRUTURAÇÃO DO GOOGLE SHEETS

Planilha pronta e estilizada na Área de Trabalho com o nome `PLANILHA_KIDOO_REVOPS_INBOUND.xlsx`:
* **Aba 1: LEADS_INBOUND_ENRIQUECIDOS:** Painel operacional com colunas para Contato, Empresa, Nicho, Faturamento, Nicho Profundo, Dor Específica, Solução Arquitetada, Precificação Sugerida e Gancho de Vendas C-Level.
* **Aba 2: VALUE_BASED_PRICING:** Matriz oficial de calibração por porte (Micro, Médio, Enterprise).
* **Aba 3: DASHBOARD_REVOPS:** Fórmulas dinâmicas somando volume e pipeline de Setup.

---

## 6. INTEGRAÇÃO NO MAKE.COM (CENÁRIO EM 4 MÓDULOS)

Blueprint salvo na Área de Trabalho com o nome `blueprint_make_kidoo.json`:
1. **Módulo 1 (Custom Webhook):** Recebe o lead da Landing Page ou Meta Ads.
2. **Módulo 2 (HTTP - Make a request):** Dispara `POST /enriquecer-lead` para o Antigravity Engine.
3. **Módulo 3 (Google Sheets - Add a Row):** Escreve a linha na planilha com a precificação calibrada.
4. **Módulo 4 (WhatsApp / Evolution API):** Alerta Pedro, Arthur ou Erick com o raio-x e gancho C-Level.

---

## 7. PASSO A PASSO PARA FAZER ACONTECER (GUIA OPERACIONAL)

### Passo 1: Iniciar o Servidor Antigravity
No terminal PowerShell:
```powershell
cd C:\Users\pedro\.gemini\antigravity-ide\scratch\kidoo-antigravity-engine
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Passo 2: Criar o Túnel Público (para o Make.com)
Em outra aba do terminal:
```powershell
npx localtunnel --port 8000
# Ou: ngrok http 8000
```
Copie a URL pública gerada (ex: `https://kidoo-revops.loca.lt`). O seu endpoint no Make será:
`https://kidoo-revops.loca.lt/enriquecer-lead`

### Passo 3: Importar a Planilha no Google Sheets
1. Acesse [sheets.new](https://sheets.new).
2. Vá em **Arquivo > Importar > Fazer upload**.
3. Selecione o arquivo `PLANILHA_KIDOO_REVOPS_INBOUND.xlsx` na sua Área de Trabalho.
4. Escolha **Substituir planilha atual**.

### Passo 4: Importar o Cenário no Make.com
1. No [Make.com](https://make.com), crie um novo cenário.
2. Clique no menu de **três pontinhos (...)** na barra inferior e escolha **Import Blueprint**.
3. Selecione `blueprint_make_kidoo.json` da sua Área de Trabalho.
4. No Módulo 2 (HTTP), cole a URL do seu túnel.
5. No Módulo 3 (Google Sheets), selecione sua planilha importada.
6. Clique em **Save** e ative a chave para **ON**.

### Passo 5: A Call de 15 Minutos C-Level
Assim que o alerta apitar no WhatsApp:
1. Veja o porte do lead e a **Precificação Sugerida** (ex: se for Enterprise, já sabe que o setup é R$ 12k+ e MRR R$ 4.5k+).
2. Abra a reunião diretamente com a pergunta do **Gancho de Vendas C-Level**, sem papo genérico de vendedor.
3. Apresente a arquitetura exclusiva da Kidoo e feche a proposta ancorada no valor milionário gerado.
