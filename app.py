import streamlit as st
from providers.data_provider import get_dados_monitoramento
from ui.components import render_metric_card
import plotly.express as px

st.set_page_config(page_title="Dashboard GS", layout="wide")

if "dados" not in st.session_state: st.session_state["dados"] = get_dados_monitoramento()

st.title("Monitoramento Espacial - Global Solution")
st.markdown("---")

st.sidebar.header("Filtros")
regiao = st.sidebar.selectbox("Região", ["Norte", "Sul", "Leste", "Oeste", "Todas"])

df = st.session_state["dados"]
if regiao != "Todas": df = df[df['Regiao'] == regiao]

render_metric_card("Focos Totais (Filtro)", int(df['Focos'].sum()), "0")

aba1, aba2 = st.tabs(["Visão Geral", "Intervenção"])

aba1.subheader("Gráfico de Focos")
fig = px.bar(df, x='Regiao', y='Focos', color='Risco')
aba1.plotly_chart(fig, use_container_width=True)

aba2.subheader("Painel de Intervenção")
aprovado = aba2.checkbox("Confirmar envio de equipe")
if aprovado: aba2.success("Equipe notificada!")
if not aprovado: aba2.info("Aguardando...")
