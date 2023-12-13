import streamlit as st

st.set_page_config(page_title="Plan de contrôle", page_icon="🗺️", layout="wide")
st.markdown("# Dimensionnement du Plan de Contrôle 🗺️")
st.sidebar.markdown("# C'est la cinquième page 🛸")

if "mean_msg_size" not in st.session_state:
    st.session_state.mean_msg_size = 0.0

st.markdown(":green[Veuillez renseigner l'information suivante avant de commencer :]")
mean_msg_size = st.number_input("Taille moyen d'un message (bits)")

st.session_state.mean_msg_size = mean_msg_size