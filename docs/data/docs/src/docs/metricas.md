# 📊 Avaliação e Métricas

## Objetivo

Avaliar a capacidade do QuimIA de responder corretamente às perguntas e evitar informações inventadas.

## Métricas utilizadas

### Assertividade

Percentual de perguntas respondidas corretamente.

```text
Assertividade =
respostas corretas / total de perguntas × 100
```

### Cobertura

Quantidade de perguntas relacionadas à base que o agente consegue responder.

### Segurança

Verifica se o agente evita inventar informações que não estão disponíveis.

### Clareza

Avalia se as respostas são compreensíveis para o público-alvo.

## Testes

Foram utilizados testes envolvendo Cálculo, Química Geral, Balanço de Massa, Física e Estatística.

Também foram realizados testes com perguntas que não estavam presentes na base.

## Critérios

O agente deve:

* Responder corretamente aos conteúdos disponíveis;
* Evitar invenções;
* Utilizar linguagem clara;
* Manter o contexto da conversa;
* Informar quando não possuir informação suficiente.
