/**
 * ========================================================================================
 * KIDOO HUB — GOOGLE APPS SCRIPT OFICIAL (CAIXA DE LEGO REVOPS)
 * ========================================================================================
 */

function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 Kidoo Hub RevOps')
    .addItem('⚙️ Estruturar / Resetar Abas com a Caixa de Lego', 'estruturarPlanilhaKidooCompleta')
    .addToUi();
}

function estruturarPlanilhaKidooCompleta() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // 1. Aba LEADS_INBOUND_ENRIQUECIDOS
  var wsLeads = ss.getSheetByName("LEADS_INBOUND_ENRIQUECIDOS");
  if (!wsLeads) {
    wsLeads = ss.insertSheet("LEADS_INBOUND_ENRIQUECIDOS", 0);
  }
  
  wsLeads.clear();
  wsLeads.setRowHeight(1, 40);
  wsLeads.getRange("A1:L1").merge()
    .setValue("🎯 KIDOO HUB — DIAGNÓSTICO HIPER-PERSONALIZADO (CAIXA DE LEGO REVOPS)")
    .setBackground("#1E1B4B")
    .setFontColor("#FFFFFF")
    .setFontSize(12)
    .setFontWeight("bold")
    .setHorizontalAlignment("center")
    .setVerticalAlignment("middle");

  var headersLeads = [
    "Data/Hora",
    "Contato",
    "Empresa",
    "Nicho",
    "Faturamento",
    "Nicho Profundo (Como Opera)",
    "Dor Específica (Ponto de Sangria)",
    "Solução Arquitetada (Caixa de Lego)",
    "Precificação Sugerida",
    "Gancho de Vendas (Call 15 min)",
    "Closer",
    "Status"
  ];
  
  wsLeads.setRowHeight(2, 32);
  wsLeads.getRange(2, 1, 1, headersLeads.length).setValues([headersLeads])
    .setBackground("#312E81")
    .setFontColor("#FFFFFF")
    .setFontSize(10)
    .setFontWeight("bold")
    .setHorizontalAlignment("center")
    .setVerticalAlignment("middle")
    .setWrap(true);

  var leadsExemplo = [
    [
      "13/10/2026 14:30",
      "Roberto Alcantara",
      "Desentupidora & Dedetizadora Plantão 24h",
      "Serviços Emergenciais e Desentupimento",
      "R$ 55.000/mês",
      "Opera sob demanda de urgência máxima (onde o primeiro que responde fecha o serviço de alto ticket imediato).",
      "Perda de chamados de madrugada e finais de semana por falta de atendente acordado e demora na triagem do endereço/orçamento.",
      "Agente de IA Conversacional (WhatsApp 24/7) + Triagem Técnica de Emergência (coleta de endereço/problema) + Automação Make.com disparando alerta sonoro para a equipe de plantão.",
      "Setup de R$ 3.500 e MRR de R$ 950/mês",
      "\"Roberto, quando um cliente com esgoto transbordando manda mensagem no WhatsApp da Desentupidora Plantão 24h às 2h da madrugada, quem atende ele em 10 segundos antes que ele ligue para o concorrente da pesquisa do Google?\"",
      "Pedro",
      "Call Agendada"
    ],
    [
      "13/10/2026 15:10",
      "Dra. Juliana Mendes",
      "Clínica Estética & Dermatologia Savassi",
      "Estética e Harmonização Facial",
      "R$ 80.000/mês",
      "Monetiza por tempo de agenda e procedimentos executados; faturamento altamente vulnerável a cadeiras ociosas.",
      "Atendimento lento em picos, secretária sobrecarregada e taxa de no-show entre 15% e 25% por confirmação manual falha.",
      "Agente de IA Conversacional 24/7 + Sincronização de Agendas bidirecional + Régua Ativa Anti-No-Show no WhatsApp + Infraestrutura Web (Landing Page Viva).",
      "Setup de R$ 2.800 e MRR de R$ 850/mês",
      "\"Dra. Juliana, quantas consultas ou procedimentos de alto ticket a Clínica Estética Savassi perde todo mês simplesmente porque a recepção demorou 15 minutos para responder ou porque o paciente esqueceu e não apareceu?\"",
      "Pedro",
      "Novo Lead"
    ]
  ];

  wsLeads.getRange(3, 1, leadsExemplo.length, headersLeads.length).setValues(leadsExemplo)
    .setFontFamily("Segoe UI")
    .setFontSize(9)
    .setVerticalAlignment("middle")
    .setWrap(true);

  var colWidths = [130, 160, 220, 190, 130, 250, 260, 300, 200, 320, 100, 120];
  for (var i = 0; i < colWidths.length; i++) {
    wsLeads.setColumnWidth(i + 1, colWidths[i]);
  }

  // 2. Aba CAIXA_DE_LEGO_TECNOLOGIAS
  var wsLego = ss.getSheetByName("CAIXA_DE_LEGO_TECNOLOGIAS");
  if (!wsLego) {
    wsLego = ss.insertSheet("CAIXA_DE_LEGO_TECNOLOGIAS", 1);
  }
  wsLego.clear();
  wsLego.setRowHeight(1, 40);
  wsLego.getRange("A1:D1").merge()
    .setValue("🧱 KIDOO HUB — NOSSAS TECNOLOGIAS BASE (SUA CAIXA DE LEGO)")
    .setBackground("#1E1B4B")
    .setFontColor("#FFFFFF")
    .setFontSize(12)
    .setFontWeight("bold")
    .setHorizontalAlignment("center")
    .setVerticalAlignment("middle");

  var headersLego = ["Tecnologia Base", "Descrição Operacional", "Líder Técnico", "Aplicação Típica"];
  wsLego.getRange(2, 1, 1, 4).setValues([headersLego])
    .setBackground("#312E81")
    .setFontColor("#FFFFFF")
    .setFontWeight("bold")
    .setHorizontalAlignment("center")
    .setVerticalAlignment("middle");

  var catalogo = [
    ["Agente de IA Conversacional (WhatsApp/Direct 24/7)", "Respostas em < 5s humanizadas, tira dúvidas, qualifica e fecha agendamento/venda.", "Pedro (Tecnologia)", "Clínicas, emergências, e-commerce, qualquer nicho"],
    ["Automação via Make.com (Webhooks e Integrações)", "Orquestração de dados entre formulários, banco de dados, CRMs e APIs proprietárias.", "Pedro (Tecnologia)", "Automação de processos e sincronização de dados"],
    ["Sincronização de Agendas (Google Calendar/Nativos)", "Agendamento bidirecional em tempo real com régua ativa anti-no-show no WhatsApp.", "Pedro (Tecnologia)", "Clínicas, salões, barbearias, consultórios"],
    ["Motor de Pix Dinâmico e Conciliação Bancária", "Geração instantânea de Pix com validação direta via webhook bancário sem fraude humana.", "Pedro (Tecnologia)", "Delivery, ingressos, taxas de reserva, sinal de serviço"],
    ["Impressão Térmica Remota (Protocolo ESC/POS)", "Impressão automática de comandas e pedidos no balcão ou cozinha assim que pago.", "Pedro (Tecnologia)", "Adegas, pizzarias, hamburguerias, lanchonetes"],
    ["Motor de Reativação de Base Antiga", "Scraping e higienização de contatos antigos com disparos segmentados e IA no retorno.", "Pedro (Tecnologia)", "Empresas com mais de 300 clientes cadastrados inativos"],
    ["Triagem Técnica (Lead Routing B2B & CRM)", "Perguntas de qualificação e algoritmo Round-Robin distribuindo leads quentes aos closers.", "Pedro (Tecnologia)", "Imobiliárias, construtoras, locadoras de máquinas, B2B"],
    ["Infraestrutura Web (Landing Pages e Sites)", "Pistas de pouso de alta conversão conectadas ao WhatsApp e sites multipáginas institucionais.", "Erick (Infraestrutura)", "Captação de leads e autoridade digital da marca"]
  ];
  wsLego.getRange(3, 1, catalogo.length, 4).setValues(catalogo)
    .setFontFamily("Segoe UI")
    .setFontSize(9)
    .setVerticalAlignment("middle");

  var legoWidths = [280, 360, 180, 320];
  for (var j = 0; j < legoWidths.length; j++) {
    wsLego.setColumnWidth(j + 1, legoWidths[j]);
  }

  SpreadsheetApp.getActiveSpreadsheet().toast("Planilha Kidoo Hub atualizada com a Caixa de Lego!", "🚀 Sucesso", 5);
}

function doPost(e) {
  try {
    var dados = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var wsLeads = ss.getSheetByName("LEADS_INBOUND_ENRIQUECIDOS");
    var dataHora = Utilities.formatDate(new Date(), "America/Sao_Paulo", "dd/MM/yyyy HH:mm");
    
    wsLeads.appendRow([
      dataHora,
      dados.nome_lead || "",
      dados.empresa || "",
      dados.nicho || "",
      dados.faturamento || "Não informado",
      dados.nicho_profundo || "",
      dados.dor_especifica || "",
      dados.solucao_arquitetada || "",
      dados.precificacao_sugerida || "",
      dados.gancho_vendas || "",
      dados.closer || "Pedro",
      "Novo Lead"
    ]);

    return ContentService.createTextOutput(JSON.stringify({ status: "sucesso" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "erro", mensagem: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
