import streamlit as st

def render_metric_card(label, value, delta): st.metric(label=label, value=value, delta=delta)