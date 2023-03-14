# PROJETO - Monitoramento de modelos de machine learning

Desenvolvimento de uma API para avaliação de performance e aderência [../monitoring/app/](../monitoring/app)

## Avaliando a API no notebook

Antes de rodar as células no notebook, inicie o servidor rodando o arquivo `monitoring\app\main.py` no ambiente Python.

![](https://github.com/LuanaPorciuncula/challenge-data-scientist/blob/main/gifs/run_server.gif)

O notebook de avaliação da API se encontra em [../monitoring/model_monitor.ipynb](../monitoring/model_monitor.ipynb)

## Respostas das perguntas acerca do projeto

1. *Se quisermos expandir o monitoramento para todos os modelos atualmente em produção, você acha que pode dar algum problema caso haja muitas requisições simultâneas ao mesmo endpoint da API? O que podemos fazer neste caso?*
 - Dependendo da quantidade de requisições simultâneas, o servidor pode ficar sobrecarregado. E uma possível solução é utilizar o Docker para escalar o projeto de monitoramento de modelos, criando containers, cada um com uma instância da aplicação do servidor, de acordo com a demanda.


2. *Que outro problema um modelo de machine learning pode enfrentar em produção, que você ache interessante monitorar?*
 - Acredito que um problema comumente enfrentado em produção pelos modelos seja o tempo gasto na execução do treinamento e predição. Talvez seja interessante expandir a API para monitorar esses tempos em cima de bases de dados de diversos tamanhos.
