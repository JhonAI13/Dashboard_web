import streamlit as st
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from io import BytesIO

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

# Carrega os dados e renomeia as colunas para padronizar
file_path = "data/vehicles.csv"
df = load_data(file_path)
df.columns = ['price', 'year', 'model', 'condition', 'cylinders', 'fuel',
              'odometer', 'transmission', 'body', 'color', 'extra', 'date', 'days']

# Converte para numérico as colunas relevantes
for col in ['price', 'year', 'cylinders', 'odometer', 'extra', 'days']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

st.title("Análise de Veículos")
st.write("""### Funcionalidades  
- Visualização dos Dados  
    Exibe o DataFrame completo com as informações dos veículos.  
- Histograma Interativo  
    Permite selecionar uma coluna numérica (preço, ano, odômetro, dias) e visualizar sua distribuição.  
- Scatter Plot Dinâmico  
    Escolha interativa das variáveis para os eixos X e Y, analisando relações entre atributos numéricos.  
- Estatísticas Descritivas  
    Exibe métricas como média, desvio padrão e quartis para melhor compreensão dos dados.  
- Mapa de Calor da Correlação (com Download)  
    Gera um heatmap das correlações entre variáveis numéricas.  
    Possibilidade de baixar o gráfico em PNG para uso posterior.  
---  
""")
# Exibição do DataFrame (opcional)
if st.checkbox("Mostrar DataFrame"):
    st.dataframe(df)

# --- Histograma ---
st.header("Histograma")
# Seletor para escolher a coluna do histograma (contendo apenas colunas numéricas relevantes)
hist_col = st.selectbox("Selecione a coluna para o histograma:", ['price', 'year', 'odometer', 'days'])
if hist_col:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df[hist_col].dropna(), bins=50, edgecolor="black")
    ax.set_title(f'Histograma de {hist_col}')
    ax.set_xlabel(hist_col)
    ax.set_ylabel("Frequência")
    st.pyplot(fig)

# --- Scatter Plot ---
st.header("Scatter Plot")
# Seletores para os eixos X e Y do scatter plot (usando todas as colunas numéricas)
num_cols = df.select_dtypes(include=np.number).columns.tolist()
x_scatter = st.selectbox("Selecione o eixo X para o Scatter Plot:", num_cols)
y_scatter = st.selectbox("Selecione o eixo Y para o Scatter Plot:", num_cols)
if x_scatter and y_scatter:
    fig, ax = plt.subplots(figsize=(8, 5))
    dados = df.dropna(subset=[x_scatter, y_scatter])
    ax.scatter(dados[x_scatter], dados[y_scatter], alpha=0.7)
    ax.set_title(f'{x_scatter} vs {y_scatter}')
    ax.set_xlabel(x_scatter)
    ax.set_ylabel(y_scatter)
    ax.grid(True)
    st.pyplot(fig)

# --- Estatísticas Descritivas ---
st.header("Estatísticas Descritivas")
if st.checkbox("Mostrar estatísticas descritivas"):
    st.write(df.describe())

# --- Mapa de Calor da Correlação com opção de Download ---
st.header("Mapa de Calor da Correlação")
if st.checkbox("Mostrar mapa de calor da correlação (download)"):
    num_df = df.select_dtypes(include=np.number).dropna()
    if not num_df.empty:
        corr = num_df.corr()
        fig, ax = plt.subplots()
        cax = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
        fig.colorbar(cax)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.index)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="left")
        ax.set_yticklabels(corr.index)
        for i in range(len(corr)):
            for j in range(len(corr)):
                ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="black")
        st.pyplot(fig)
        buf = BytesIO()
        fig.savefig(buf, format="png")
        st.download_button("Download mapa de calor", data=buf.getvalue(),
                           file_name="heatmap.png", mime="image/png")
    else:
        st.write("Dados numéricos insuficientes para gerar o mapa de calor.")
