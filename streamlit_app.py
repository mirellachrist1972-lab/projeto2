# MVP mirella
#Projeto de MVP para agiula de ferramentas e soluções em nuvem
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Atividade 01:
# Fazer seu primeiro web app com o streamlit, devendo realizar o deploy e postar o link
# Este app-web deverá conter:
# 1) Seu nome
# 2) um tema que pretende tratar
# 3) A divisão das seções do app, prevendo futura expansão para apresentar dados e gráficos.
# 4) Bases de dados que imagina usar

st.title("🚀 Iniciando meu primeiro app")
st.write ('**Distribuição do PROGEFE nas escolas estaduais do ES em 2024.**')
st.text ('')
st.markdown ('📌 **Aluna**')
st.text ('Mirella Carla Mendes Christ')

# Configuração inicial da página
st.set_page_config(
    page_title="Distribuição do PROGEFE",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("Análise dos valores do PROGEFE em 2024")
st.markdown("---")

# Seção 1: Apresentação
st.header("Desenvolvedora")
st.write("*Mirella Carla Mendes Christ*")

# Seção 2: Tema do projeto
st.header("Tema do Projeto")
st.write("Distribuição dos recursos financeiros distribuidos através do PROGEFE nas escolas estaduais do ES em 2024, com dashboards regionais e por escolas e superintendências.")
st.write("Dados fictícios")

# Seção 3: Estrutura do aplicativo
st.header("Estrutura do Aplicativo")
st.write("O aplicativo será organizado nas seguintes seções:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📈 Dashboard por município")
    st.write("Visualização de valores em R$ por região geográfica")

with col2:
    st.subheader("🏫 Dashboard por Escola")
    st.write("Análise detalhada de valores em R$ por unidade escolar")

# Seção 4: Bases de dados
st.header("Bases de Dados")
st.write("Fontes de dados que serão utilizadas no projeto:")

st.markdown("""
- Valores de distribuição dos recursos do sistema e-gestão
- Registros de Instituições de Ensino
- Dados dos valores por município """)

# Seção 5: Próximas etapas
st.header("Próximas Etapas")
st.write("Para versões futuras, planejamos implementar:")

st.markdown("""
1. Gráficos dos valores por escola
2. Gráficos dos valores por município
3. Dados estatísticos
""")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Mirella Carla Mendes Christ - 2025")

# Título do aplicativo
st.title("Análise de Arrecadação por Escola e Município")

# Carregar dataset
@st.cache_data
def carregar_dados(name):
    df = pd.read_csv(name)
    return df

df = carregar_dados("dados_escolas.csv")

st.subheader("Dados Originais")
st.dataframe(df)

regiao_selecionada = st.sidebar.multiselect(
    "Selecionar Região",
    options=df["mun"].unique(),
    default=df["mun"].unique()
)

# Aplicar filtros globais
df_filtrado_global = df[
    (df["mun"].isin(regiao_selecionada))
]

st.subheader(" Visão Geral dos Dados")
st.dataframe(df_filtrado_global.head())

# 1. Gráfico de Barras: Valor arrecadado por Escola
st.subheader("Valor Arrecadado por Escola")
fig_escola, ax_escola = plt.subplots(figsize=(12, 7))
sns.barplot(x="nome_esc", y="val", data=df.sort_values(by="val", ascending=False).head(20), ax=ax_escola, palette="viridis")
ax_escola.set_xlabel("Nome da Escola")
ax_escola.set_ylabel("Valor Arrecadado R$")
ax_escola.set_title("Top 20 Escolas por maior valor arrecadado")
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
st.pyplot(fig_escola)

# 2. Gráfico de Barras: Valor arrecadado por Município
st.subheader("Valor Arrecadado por Município")

# Agrupar por município e somar os valores
df_municipio_agg = df.groupby("mun")["val"].sum().reset_index()
fig_municipio, ax_municipio = plt.subplots(figsize=(12, 7))
sns.barplot(x="mun", y="val", data=df_municipio_agg.sort_values(by="val", ascending=False), ax=ax_municipio, palette="magma")
ax_municipio.set_xlabel("Município")
ax_municipio.set_ylabel("Valor Total Arrecadado em R$")
ax_municipio.set_title("Valor total arrecadado pelas escolas e por munícíopio R$")
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
st.pyplot(fig_municipio)

# Estatísticas Descritivas
st.subheader("Estatísticas Descritivas")
st.write(df.describe())

