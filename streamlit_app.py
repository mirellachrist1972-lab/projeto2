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
st.title("Análise dos valores do PROGEFE em 2025")
st.markdown("---")

# Seção 1: Apresentação
st.header("Desenvolvedora")
st.write("*Mirella Carla Mendes Christ*")

# Seção 2: Tema do projeto
st.header("Tema do Projeto")
st.write("Distribuição dos recursos financeiros distribuidos através do PROGEFE nas escolas estaduais do ES em 2024, com dashboards regionais e por escolas e superintendências.")

# Seção 3: Estrutura do aplicativo
st.header("Estrutura do Aplicativo")
st.write("O aplicativo será organizado nas seguintes seções:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📈 Dashboard Regional")
    st.write("Visualização de valores em R$ por região geográfica")

with col2:
    st.subheader("🏫 Dashboard por Escola")
    st.write("Análise detalhada de valores em R$ por unidade escolar")

with col3:
    st.subheader("👥 Dashboard por Superintendência")
    st.write("Visualização dos valores em R$ por superintendências regionais")

# Seção 4: Bases de dados
st.header("Bases de Dados")
st.write("Fontes de dados que serão utilizadas no projeto:")

st.markdown("""
- Valores de distribuição dos recursos do sistema e-gestão
- Registros de Instituições de Ensino
- Dados dos valores por Superintendência """)

# Seção 5: Próximas etapas
st.header("Próximas Etapas")
st.write("Para versões futuras, planejamos implementar:")

st.markdown("""
1. Gráficos interativos de evolução de matrículas
2. Comparativos entre anos letivos
3. Indicadores de taxa de ocupação por escola
4. Previsões de demanda para próximos períodos
5. Relatórios personalizados para gestores
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

# 1. Gráfico de Barras: Valor arrecadado por Escola
st.subheader("Valor Arrecadado por Escola")
fig_escola, ax_escola = plt.subplots(figsize=(12, 7))
sns.barplot(x="nome_esc", y="val", data=df.sort_values(by="val", ascending=False).head(20), ax=ax_escola, palette="viridis")
ax_escola.set_xlabel("Nome da Escola")
ax_escola.set_ylabel("Valor Arrecadado")
ax_escola.set_title("Top 20 Escolas por Valor Arrecadado")
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
ax_municipio.set_ylabel("Valor Total Arrecadado")
ax_municipio.set_title("Valor Total Arrecadado por Município")
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
st.pyplot(fig_municipio)

# Estatísticas Descritivas
st.subheader("Estatísticas Descritivas")
st.write(df.describe())

