# Análise de Churn de Clientes

Este projeto foi desenvolvido como parte do Challenge de Ciência de Dados da Alura. O objetivo principal é realizar uma análise exploratória para compreender os fatores que levam ao cancelamento de clientes em uma empresa fictícia de telecomunicações.

## Objetivos

- Aplicar as etapas de um pipeline de dados: extração, transformação, carga e análise.
- Identificar padrões e variáveis associadas ao churn.
- Utilizar bibliotecas e ferramentas comuns no ecossistema de dados com Python.
- Desenvolver visualizações que auxiliem na interpretação dos dados.

## Etapas do Projeto

### 1. Extração

- Importação do conjunto de dados em formato CSV.
- Leitura inicial e verificação das primeiras amostras.

### 2. Transformação

- Tratamento de valores ausentes e inconsistentes.
- Conversão de colunas para os tipos de dados apropriados.
- Padronização de nomes e categorias.

### 3. Carga

- Salvamento do dataset limpo em um novo arquivo CSV para reutilização.
- Organização do DataFrame final para análise e visualização.

### 4. Análise Exploratória

- Geração de gráficos para investigar a relação entre o churn e variáveis como:
  - Tipo de contrato
  - Serviços contratados
  - Forma de pagamento
  - Tempo de permanência
- Comparação de distribuições entre clientes que cancelaram e os que permaneceram.
- Identificação de padrões relevantes para a área de negócio.

## Ferramentas Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Organização do Projeto

- `notebooks/`: arquivos de análise e limpeza dos dados
- `dados/`: dataset original
- `relatorio/`: relatório final do projeto em HTML
- `visualizacoes/`: imagens e gráficos gerados na análise

## Conclusão

O projeto permitiu explorar práticas de análise de dados e manipulação de datasets reais, fornecendo insights importantes sobre o comportamento dos clientes. As visualizações ajudaram a destacar fatores associados ao churn e a preparar o terreno para futuras análises preditivas.

## Autor

Desenvolvido por Henry (just fontaine) como parte do programa de formação em Ciência de Dados da Oracle em conjunto com a Alura.
