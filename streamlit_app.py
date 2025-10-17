# Projeto de MVP para análise de ferramentas e soluções em nuvem
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configuração inicial da página
st.set_page_config(
    page_title="Distribuição do PROGEFE",
    page_icon="📊",
    layout="wide"
)

# Função para carregar dados com validação
@st.cache_data
def carregar_dados(file_name):
    """Carrega um arquivo CSV e retorna um DataFrame pandas.
    
    Args:
        file_name (str): Caminho do arquivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    try:
        df = pd.read_csv(file_name)
        required_columns = ["nome_esc", "mun", "val"]
        if not all(col in df.columns for col in required_columns):
            st.error("O arquivo CSV não contém todas as colunas necessárias: 'nome_esc', 'mun', 'val'.")
            st.stop()
        # Renomear colunas para maior clareza
        df = df.rename(columns={
            "nome_esc": "nome_escola",
            "mun": "municipio",
            "val": "valor_arrecadado"
        })
        return df
    except FileNotFoundError:
        st.error(f"Arquivo '{file_name}' não encontrado.")
        st.stop()
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        st.stop()

# Função para plotar valor por escola
def plot_valor_por_escola(df, top_n=20):
    """Gera um gráfico de barras com os valores arrecadados por escola."""
    if df.empty:
        st.warning("Nenhum dado disponível para o gráfico de escolas.")
        return
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(
        x="nome_escola",
        y="valor_arrecadado",
        data=df.sort_values(by="valor_arrecadado", ascending=False).head(top_n),
        ax=ax,
        palette="viridis"
    )
    ax.set_xlabel("Nome da Escola")
    ax.set_ylabel("Valor Arrecadado (R$)")
    ax.set_title(f"Top {top_n} Escolas por Valor Arrecadado")
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)

# Função para plotar valor por município
def plot_valor_por_municipio(df):
    """Gera um gráfico de barras com os valores arrecadados por município."""
    if df.empty:
        st.warning("Nenhum dado disponível para o gráfico de municípios.")
        return
    df_agg = df.groupby("municipio")["valor_arrecadado"].sum().reset_index()
    df_agg = df_agg.sort_values(by="valor_arrecadado", ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(
        x="municipio",
        y="valor_arrecadado",
        data=df_agg,
        ax=ax,
        palette="magma"
    )
    ax.set_xlabel("Município")
    ax.set_ylabel("Valor Total Arrecadado (R$)")
    ax.set_title("Valor Total Arrecadado por Município (R$)")
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)

# Função para exibir estatísticas descritivas
def exibir_estatisticas(df):
    """Exibe estatísticas descritivas formatadas."""
    if df.empty:
        st.warning("Nenhum dado disponível para estatísticas.")
        return
    stats = df[["valor_arrecadado"]].describe().reset_index().rename(columns={"index": "Estatística"})
    st.table(stats)

# Carregar dataset
df = carregar_dados("dados_escolas.csv")

# Índice interativo com st.radio
st.sidebar.subheader("Navegação")
sections = [
    "Iniciando meu primeiro app",
    "Tema do Projeto",
    "Estrutura do Aplicativo",
    "Bases de Dados",
    "Próximas Etapas",
    "Análise de Arrecadação por Escola e Município",
    "Visão Geral dos Dados",
    "Valor Arrecadado por Escola",
    "Valor Arrecadado por Município",
    "Estatísticas Descritivas"
]
selected_section = st.sidebar.radio("Ir para a seção:", sections, index=0)# Configuração da sidebar com filtros e índice
st.sidebar.subheader("Filtros")
municipios_unicos = df["municipio"].unique().tolist()
regiao_selecionada = st.sidebar.multiselect(
    "Selecionar Municípios",
    options=municipios_unicos,
    default=municipios_unicos
)

# Botão para selecionar todos
if st.sidebar.button("Selecionar Todos os Municípios"):
    regiao_selecionada = municipios_unicos

# Aplicar filtros
df_filtrado = df[df["municipio"].isin(regiao_selecionada)]


# Exibir conteúdo com base na seção selecionada
st.markdown("---")
if selected_section == "Iniciando meu primeiro app":
    st.title("🚀 Iniciando meu primeiro app")
    st.write('**Distribuição do PROGEFE nas escolas estaduais do ES em 2024.**')
    st.text('')
    st.markdown('📌 **Aluna: Mirella Carla Mendes Christ**')
  
elif selected_section == "Tema do Projeto":
    st.header("Tema do Projeto")
    st.write("Distribuição dos recursos financeiros distribuídos através do PROGEFE nas escolas estaduais do ES em 2024, com dashboards regionais e por escolas e superintendências.")
    st.write("Dados fictícios")

elif selected_section == "Estrutura do Aplicativo":
    st.header("Estrutura do Aplicativo")
    st.write("O aplicativo será organizado nas seguintes seções:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📈 Dashboard por município")
        st.write("Visualização de valores em R$ por região geográfica")
    with col2:
        st.subheader("🏫 Dashboard por Escola")
        st.write("Análise detalhada de valores em R$ por unidade escolar")

elif selected_section == "Bases de Dados":
    st.header("Bases de Dados")
    st.write("Fontes de dados que serão utilizadas no projeto:")
    st.markdown("""
    - Valores de distribuição dos recursos do sistema e-gestão
    - Registros de Instituições de Ensino
    - Dados dos valores por município
    """)

elif selected_section == "Próximas Etapas":
    st.header("Próximas Etapas")
    st.write("Para versões futuras, planejamos implementar:")
    st.markdown("""
    1. Gráficos interativos com zoom e tooltips
    2. Integração com APIs para dados em tempo real
    3. Exportação de relatórios em PDF
    4. Filtros adicionais (por escola, valor mínimo/máximo)
    5. Visualizações geográficas (mapas)
    """)

elif selected_section == "Análise de Arrecadação por Escola e Município":
    st.title("Análise de Arrecadação por Escola e Município")
    st.subheader("Dados Originais")
    st.dataframe(df, height=400)

elif selected_section == "Visão Geral dos Dados":
    st.subheader("Visão Geral dos Dados")
    st.dataframe(df_filtrado.head(), height=400)
    # Botão de download
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Baixar Dados Filtrados (CSV)",
        data=csv,
        file_name="dados_filtrados_progefe.csv",
        mime="text/csv"
    )

elif selected_section == "Valor Arrecadado por Escola":
    st.subheader("Valor Arrecadado por Escola")
    plot_valor_por_escola(df_filtrado)

elif selected_section == "Valor Arrecadado por Município":
    st.subheader("Valor Arrecadado por Município")
    plot_valor_por_municipio(df_filtrado)

elif selected_section == "Estatísticas Descritivas":
    st.subheader("Estatísticas Descritivas")
    exibir_estatisticas(df_filtrado)