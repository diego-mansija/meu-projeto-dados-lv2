import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da Página e Estética
st.set_page_config(page_title="meu-projeto-dados | Vendas", layout="wide")

# Mock de Dados
@st.cache_data
def get_data():
    data = {
        'Data': pd.to_datetime(['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04']),
        'Categoria': ['Eletrônicos', 'Moda', 'Eletrônicos', 'Casa'],
        'Venda': [1500, 200, 1200, 450],
        'Quantidade': [2, 5, 1, 3]
    }
    return pd.DataFrame(data)

df = get_data()

# Sidebar (Filtros Interativos)
st.sidebar.header("Painel de Controle")
st.sidebar.info("Use os filtros abaixo para atualizar os gráficos em tempo real.")

categorias = st.sidebar.multiselect(
    "Filtrar por Categoria:",
    options=df['Categoria'].unique(),
    default=df['Categoria'].unique()
)

# Filtrando o dataframe com base na seleção
df_filtrado = df[df['Categoria'].isin(categorias)]

# Layout de Métricas
st.title("Dashboard de Performance de Vendas")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    total_vendas = df_filtrado['Venda'].sum()
    st.metric(label="Faturamento Total", value=f"R$ {total_vendas:,.2f}")

with col2:
    qtd_total = df_filtrado['Quantidade'].sum()
    st.metric(label="Produtos Vendidos", value=qtd_total)

with col3:
    ticket_medio = total_vendas / qtd_total if qtd_total > 0 else 0
    st.metric(label="Ticket Médio", value=f"R$ {ticket_medio:,.2f}")

st.markdown("---")

# Gráficos
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("Vendas por Categoria")
    fig, ax = plt.subplots(figsize=(8, 5))
    # Usando o seu conhecimento em Matplotlib:
    df_filtrado.groupby('Categoria')['Venda'].sum().plot(kind='bar', ax=ax, color='#4B8BBE')
    ax.set_ylabel("Valor (R$)")
    ax.set_xlabel("Categoria")
    st.pyplot(fig)

with col_dir:
    st.subheader("Visualização da Tabela")
    st.dataframe(df_filtrado, use_container_width=True)

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("Desenvolvido para o Portfólio de Dados")