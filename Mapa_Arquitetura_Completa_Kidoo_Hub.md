# 🗺️ MAPA DE ARQUITETURA FIM A FIM: PROJETO "CASO ZERO" (KIDOO HUB)
**Versão:** 2.0 (Full Stack Vision)  
**Objetivo:** Mapeamento completo do ecossistema, desde o clique no anúncio até a assinatura do contrato e o setup.

---

## 🚁 VISÃO MACRO DO FUNIL
O "Caso Zero" é um loop autônomo dividido em 5 Fases Operacionais. A intervenção humana só acontece na Fase 1 (Configuração da Campanha), na Fase 4 (Acompanhamento no CRM) e na Fase 5 (A Call de Fechamento). Todo o "meio de campo" é orquestrado pelo Antigravity, Make.com e Gemini.

---

## 📍 FASE 1: AQUISIÇÃO E POUSO (TRAÇÃO)
**Responsáveis:** Arthur (Tráfego) e Erick (Infraestrutura Web)
1. **O Anúncio:** Arthur roda campanhas no Meta Ads e Google Ads com segmentação B2B (donos de clínicas, construtoras, distribuidoras).
2. **A Pista de Pouso:** O lead clica e cai na Landing Page focada em conversão construída pelo Erick.
3. **A Captura:** O lead preenche o formulário (Nome, Empresa, Nicho, Faturamento, WhatsApp).
4. **O Gatilho:** Ao clicar em "Enviar", a Landing Page dispara um Webhook silencioso para o Make.com.

---

## 🧠 FASE 2: CENÁRIO 1 (LATÊNCIA ZERO & ANTIGRAVITY)
**Responsável:** Pedro (Tecnologia/Make.com)
*Ocorre em menos de 10 segundos.*

1. **Recepção:** Make.com recebe o Webhook da Landing Page.
2. **Cérebro Antigravity:** O Make envia os dados para o Gemini (Prompt C-Level Value-Based Pricing).
3. **Saída JSON:** O Gemini devolve instantaneamente: Nicho Profundo, Dor Específica, Solução Kidoo Arquitetada, Preço Calibrado (Setup + MRR) e o Gancho de Vendas.
4. **Gravação no Cofre:** O Make salva essa linha completa na planilha `LEADS_INBOUND_ENRIQUECIDOS` no Google Sheets (ID: `1PRprGhbag7oxvoIG_zrDjXQSupadKIgBguMinkdHzrg`). Status = "1 - Inbound Cru".
5. **Primeiro Contato:** O Make manda um comando para a API do WhatsApp disparar a mensagem de boas-vindas: *"Fala [Nome], recebi seu contato... "*
6. **Alerta C-Level:** Disparo no Telegram/WhatsApp dos sócios avisando: *"Novo Lead B2B. Empresa X. Dor Y. Ticket Z."*

---

## 🤖 FASE 3: CENÁRIO 2 (MOTOR CONVERSACIONAL SDR & AGENDA)
**Responsável:** Pedro (Tecnologia/Make.com)
*O loop contínuo. Entra em ação assim que o lead responde a mensagem de boas-vindas.*

1. **Escuta Ativa (Webhook):** O lead manda mensagem de texto ou áudio no WhatsApp da Kidoo. A API joga pro Make.
2. **Transcrição (Whisper):** Se for áudio, o Make converte em texto.
3. **Reconhecimento (Search Row):** O Make vai no Google Sheets e "puxa" a ficha desse lead (A dor dele, a solução Kidoo pensada e o porte).
4. **Disponibilidade (Calendar):** O Make consulta o Google Calendar dos sócios e pega os horários livres das próximas 72 horas.
5. **Decisão SDR (Gemini):** O Gemini analisa a resposta do lead, o contexto do Sheets e os horários livres. Ele formula uma resposta persuasiva.
6. **Router (Bifurcação):**
   - *Caminho A (Conversa em andamento):* Se o lead está apenas tirando dúvida, o Gemini devolve a resposta no WhatsApp e encerra o ciclo.
   - *Caminho B (Agendamento Confirmado):* Se o lead escolheu o horário, o Make cria o evento no Google Meet, convida o lead, envia o link no WhatsApp e atualiza o status na planilha para "3 - Call Agendada".

---

## 📊 FASE 4: KIDOO REVENUE CRM & CADÊNCIA (FOLLOW-UP)
**Responsável:** Erick (CRM)
*Para leads que não agendaram de primeira ou para o pós-call.*

1. **Gestão Visual:** A planilha do Google Sheets é espelhada no sistema de CRM do Erick (cards no estilo Kanban).
2. **Estágios do Funil:**
   - Leads Enriquecidos
   - Abordagem C-Level
   - Call Agendada
   - Proposta Enviada
   - Follow-up Ativo
   - Ganho / Perdido
3. **Régua de Follow-up (Termômetro):** Se um lead ficar mais de 48h sem responder, o card fica vermelho. O closer (sócio responsável) aperta o "Botão de Follow-up" que dispara cadências (D+1, D+3, D+5) para esquentar o lead novamente.

---

## 💼 FASE 5: CALL COMERCIAL, CLOSING E TRANSIÇÃO
**Responsáveis:** Pedro, Arthur ou Erick
*O fechamento do negócio.*

1. **A Reunião (15 minutos):** O sócio entra no Google Meet já com a "colinha" do Antigravity aberta.
2. **O Gancho:** Abre a call batendo exatamente na "Dor Específica" que a IA deduziu na Fase 2.
3. **Apresentação do Preço (Value-Based Pricing):** 
   - Micro: R$ 2k-3k Setup | R$ 600-800 MRR
   - Médio: R$ 4k-6k Setup | R$ 1.5k-2.5k MRR
   - Corporate: R$ 10k-15k Setup | R$ 3.5k-6k MRR
4. **Fechamento (Ganho):** Lead diz SIM. Pix do Setup é gerado.
5. **Transbordo (Onboarding):** O status do CRM vai para "Fechado/Ganho". O contrato é assinado e o cliente passa para a esteira técnica (Setup da automação, tráfego ou infraestrutura).
