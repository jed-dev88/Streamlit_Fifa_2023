import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"]>0]
    df_data = df_data.sort_values(by="Overall",ascending=False)
    st.session_state["data"] = df_data


st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [JedDev](https://github.com/jed-dev88/jed-dev88)")

btn = st.button("Acesso os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
        Esse dataset do FIFA 23 contém dados limpos sobre jogadores do jogo, 
        incluindo atributos detalhados como nacionalidade, posição, clubes, avaliações de habilidade 
        e características físicas. É útil para análises de desempenho, estudos de comparações 
        entre jogadores e clubes, além de modelagens de machine learning para previsão de pontuações 
        e desenvolvimento de habilidades dos jogadores.

        Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para
        analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos
        do mundo do futebol, pois permite avaliar informações de atributos de jogadores, métricas de desempenho
        , avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do 
        jogador ao longo do tempo.

    """
)