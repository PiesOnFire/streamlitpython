import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('BD_PARTOS_corrigido.xlsx')

st.sidebar.title('🍃 BD Partos')
st.sidebar.write('Análise detalhada sobre o banco de dados.')
st.sidebar.write('a. Erick')

st.title('📊 Dashboard')

#Criando colunas para a dashboard
col1, col2 = st.columns(2)

col1.metric(label="Total de Partos", value=int(df.PARTOS.sum()))

medianDURINT = int(df.DURACAO_INT.str.replace(',', '.').astype(float).median())

col2.metric(label="Mediana de Duração das Internações", value=medianDURINT)

col1.metric(label="Gravidezes de Alto Risco", value=int((df.ALTO_RISCO == "Sim").sum()))

col2.metric(label="Recém-nascidos abaixo do peso", value=(df.BAIXO_PESO == "Sim").sum())

#Função para mostrar % junto de seu respectivo valor
def func(pct, allvals):
    absolute = int(round(pct/100.*sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

#Gráfico de Pizza sobre a proporção dos nascidos vivos por gestação
fig, ax = plt.subplots()

col1.title('Nascidos vivos por gestação')
ax.pie(df.VIVO.value_counts(), autopct=lambda pct: func(pct, df.VIVO.value_counts()), startangle=90, colors=['#8C0073', '#0E0E76'])
ax.legend(labels=["Vivos","Mortos"])
col1.pyplot(fig)

#Gráfico de Pizza sobre a proporção de gravidezes com infecção/ões
fig, ax = plt.subplots()

col2.title('Proporção de gravidezes com infecção/ões')
ax.pie(df.CM_INFECCAO.value_counts(), autopct=lambda pct: func(pct, df.CM_INFECCAO.value_counts()), startangle=90, colors=['#00BBC8', '#FFB449',])
ax.legend(labels=["Sem Infec.","Com Infec."])
col2.pyplot(fig)

#Gráfico de Pizza sobre a proporção dos sexos dos recém-nascidos
fig, ax = plt.subplots()

col1.title('Proporção dos sexos dos recém-nascidos')
ax.pie(df.SEXO.value_counts(), autopct=lambda pct: func(pct, df.SEXO.value_counts()), startangle=90, colors=['#F76D4D', '#D02560'])
ax.legend(labels=["Masculino","Feminino"])
col1.pyplot(fig)

#Gráfico de Barras sobre os tipos de partos
fig, ax = plt.subplots()

col2.title('Tipos de Partos e suas Quantidades')
df.TIPO_PARTO.value_counts().plot.barh(ax=ax, color=['#FFB449', '#D02560'])
ax.set_ylabel('')
ax.grid(axis="x", linestyle="--", alpha=1, color='black')
col2.pyplot(fig)

#Histograma dos pesos dos recém-nascidos
fig, ax = plt.subplots()

st.title('Peso em gramas dos recém-nascidos')
ax.hist(df.PESO_NASCER, bins=30, color='#D02560')
ax.set_xlabel('Peso em gramas')
ax.set_ylabel('Quantidade de recém-nascidos')
ax.grid(axis="y", linestyle="--", alpha=1, color='black')
st.pyplot(fig)