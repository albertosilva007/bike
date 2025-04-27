import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do App
st.title("🚲 Estações de Bike - Data Storytelling")

# Carregando os dados
df = pd.read_csv('estacoesbike.csv', sep=';')


# Mostrar uma prévia dos dados
st.subheader("📋 Dados das Estações")
st.dataframe(df)

# Exibindo o mapa
st.subheader("🗺️ Localização das Estações")
st.map(df[['latitude', 'longitude']])

# Gráfico de capacidade por estação
st.subheader("🚲 Capacidade das Estações de Bike")

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(df['nome'], df['capacidade'], color='mediumseagreen')
plt.xticks(rotation=45, ha='right')
ax.set_xlabel('Estações')
ax.set_ylabel('Capacidade')
ax.set_title('Capacidade de cada Estação')
st.pyplot(fig)

# Insights e sugestões
st.subheader("🔍 Insights e Possíveis Soluções")
st.write("""
- Estações com maior capacidade podem ser priorizadas para manutenção e expansão de frota.
- Analisar a localização de estações de baixa capacidade para possível redistribuição.
- Novas estações podem ser implantadas em regiões sem cobertura para aumentar a acessibilidade.
""")
