# Obtenção de Informações de Ações Brasileiras

###
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](https://opensource.org/licenses/MIT) 

### Sobre:

Elaboração de um script (algoritmo) visando à automatização do processo de obtenção de informações das principais ações brasileiras.

### Proposta:

Desenvolver um script para automatizar a coleta de dados das principais ações brasileiras, **ITUB4**; **BBDC4**; **VALE3**; **PETR4**; **ABEV3** e **BBAS3**. 

Através da utilização das bibliotecas **Pandas** e **YFinance**, o script busca informações atualizadas diretamente do site de referência, <a href="https://br.financas.yahoo.com/">**Yahoo Finanças Brasil**</a> e organiza os resultados em um arquivo **xlsx**.

### Linguagem Utilizada:
###
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white&color=black)

### Bibliotecas Utilizadas:
###
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white&color=black) 	![YFinance](https://img.shields.io/badge/YFinance-%233F4F75.svg?style=for-the-badge&logoColor=white&color=black)

### Metodologia:

O script foi projetado para aceitar uma lista com o nome das ações que seriam buscada as informações. Para cada item na lista, ele faz uma consulta através da biblioteca **yfinance** para obter os dados mais recentes, como preço de abertura, preço de fechamento, entre outros.
###
Após a coleta dos dados, o script utiliza a biblioteca **Pandas** para criar um **DataFrame** contendo as informações das ações.
###
<img src="/img/dataframe_inicial.png">

###
Em seguida faz o tratamento dos dados.
###
<img src="/img/dataframe_final.png">

###
A execução bem-sucedida do script, os dados das ações são coletados e organizados em um arquivo **xlsx**.

### Conclusão:

A automação da coleta de dados de ações usando a biblioteca **YFinance** oferece uma maneira eficiente e precisa de obter informações financeiras atualizadas. A exportação dos resultados para um arquivo **xlsx** amplia a utilidade do script, permitindo a análise posterior dos dados em um formato conveniente.

---
### Contato:

<div>
  <a href="https://linkedin.com/in/marcospontesjunior" target="_blank"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white&color=black" target="_blank"></a>  
  <a href = "mailto:marcospntsjunior@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&color=black" target="_blank"></a>
</div>


