# 🧪 QuimIA — Assistente de Estudos para Engenharia Química

Assistente virtual baseado em Inteligência Artificial desenvolvido para auxiliar estudantes de Engenharia Química.

## 🎯 Objetivo

O QuimIA utiliza IA generativa e uma base de conhecimento para responder dúvidas acadêmicas de maneira clara e contextualizada.

## 💡 Problema

Estudantes precisam consultar diferentes livros, apostilas e materiais para compreender conteúdos de diversas disciplinas.

O QuimIA busca centralizar parte desse apoio em uma aplicação simples.

## 🚀 Funcionalidades

* 💬 Chat interativo;
* 🧠 Inteligência Artificial generativa;
* 📚 Base de conhecimento;
* 🔎 Respostas contextualizadas;
* 🛡️ Redução de alucinações;
* 📖 Explicações didáticas;
* 🎯 Sugestão de próximos passos.

## 📚 Conteúdos

A versão inicial possui conteúdos sobre:

* Cálculo;
* Química Geral;
* Balanço de Massa;
* Física;
* Estatística.

## 🏗️ Arquitetura

```text
Usuário
   ↓
Streamlit
   ↓
System Prompt
   ↓
Base de Conhecimento
   ↓
LLM
   ↓
Resposta
```

## 🛠️ Tecnologias

* Python
* Streamlit
* JSON
* OpenAI API
* Git
* GitHub

## 📂 Estrutura

```text
quimia-assistente-ia/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── base_conhecimento.json
│
├── docs/
│   ├── documentacao.md
│   ├── prompts.md
│   ├── metricas.md
│   └── pitch.md
│
└── src/
    └── app.py
```

## ▶️ Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a chave da API:

```powershell
$env:OPENAI_API_KEY="SUA_CHAVE"
```

Execute:

```bash
streamlit run src/app.py
```

## 📊 Avaliação

O projeto considera:

* Assertividade;
* Cobertura;
* Segurança;
* Clareza.

Também são realizados testes com perguntas presentes e ausentes na base de conhecimento.

## 🔮 Melhorias futuras

* RAG;
* Embeddings;
* Busca semântica;
* Upload de PDFs;
* Histórico de estudos;
* Recomendações personalizadas;
* Testes automatizados;
* Deploy online.

## 📌 Conclusão

O QuimIA demonstra uma aplicação prática de IA generativa combinada com uma base de conhecimento e uma aplicação web.

O projeto aborda documentação, engenharia de prompts, desenvolvimento de aplicação, avaliação, segurança e apresentação de uma solução baseada em Inteligência Artificial.

