

# **Datasets**

- O banco de dados de futebol definitivo para análise de dados,transformação e carregamento dos mesmos conta com +25.000 partidas,+10.000 jogadores, 11 países europeus com seu campeonato líder
Temporadas 2008 a 2016;
- Atributos de jogadores e equipes provenientes da série de videogames FIFA da EA Sports, incluindo as atualizações semanais;
- Alinhamento da equipe com a formação do esquadrão (coordenadas X, Y).Probabilidades de apostas de até 10 provedores e ;
- Eventos detalhados da partida (tipos de gol, posse de bola, escanteio, cruzamento, faltas, cartões etc…) para +10.000 partidas

# **Informações dos dados:**

Os dados encontram-se armazenados no arquivo **data** deste repositório. Este diretório contém os seguintes arquivos:

1. (🔎) Country.csv(*Arquivo de dados*)
2. (🔎) League.csv (*Arquivo de dados*)
3. (🔎) Match.csv (*Arquivo de dados*)
4. (🔎) Player.csv (*Arquivo de dados*)
5. (🔎) Player_Attributes.csv (*Arquivo de dados*)
6. (🔎) Team.csv (*Arquivo de dados*)
7. (🔎) Team_Attributes.csv (*Arquivo de dados*)

Colocar esses arquivos em uma Pasta chamada Data

# **Estratégias:**
-Extração dos CSVs através da classe ConvertFile.py

-Análise para arquivos csv de forma única sob um arquivo ipynb em cima de possíveis detecções para posterior tratamento, utlizando a classe DataAnalyze.py

-Tratamento dos dados para cada CSV

-Análise de dados com os dados tratados

-Carregamento dos dados 
