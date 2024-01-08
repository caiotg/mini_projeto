# Dashboard mini-projeto

A proposta desse dashboard é apresentar duas seções: cotações e notícias. Ambas seções estão ligadas a um dropdrown que escolhe uma das 3 ações disponíveis. A seção de cotações é composta por um gráfico de candles com infomações de abertura, fechamento, máxima e mínima. A seção de notícias contém as últimas três notícias publicadas pelo Brazil Journal para ação escolhida.

Os arquivos CSV utilizados para o armazenamento dos dados são atualizados através do arquivo rotinas_diarias.py dentro da pasta rotinas. A estrutura principal do Dashboard está no arquivo formato.py e os layouts do gráfico de candle e das notícias estão dentro da pasta components.

## Observações:

A fonte de dados escolhida para pegar as cotações é a API Yahoo Finance, escolhi essa fonte pois não vi necessidade de usar o MetaTrader5 para esse projeto. O scraping do Brazil jornal é feito atráves das bibliotecas Selenium e Beautifulsoup. O projeto foi estruturado de uma forma para menter a organização, visando facilitar o etendimento. A estrutura do projeto foi dividida em quatro pastas:

* assets: A pasta "assets" contém o arquivo CSS relacionado ao estilo do projeto.
* components: A pasta "components" é destinada a armazenar os layouts e callbacks de cada seção do projeto.
* dados: A pasta "dados" contém os arquivos CSV que alimentam o Dashboard.
* rotinas: Na pasta "rotinas", você encontra os arquivos responsáveis pela atualização dos CSV presentes na pasta "dados".
