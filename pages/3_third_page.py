import streamlit as st
import pandas as pd

st.set_page_config(page_title="VPN", page_icon="🌐", layout="centered")
st.markdown("# Les VPN c'est comme des ninjas 🐱‍👤")
st.sidebar.markdown("# C'est la troisième page 🎭")
st.markdown("## Trafic total pour VPN et Internet à l'Heure Chargée en Downlink et Uplink")

st.markdown(":green[**Avant de commencer nous avons besoin de certaines infos :**]")

# Initialiser l'état de la session pour cette page
if "total_subscribers" not in st.session_state:
    st.session_state.total_subscribers = None

if "percentage_data_card" not in st.session_state:
    st.session_state.percentage_data_card = None

if "percentage_smartphone" not in st.session_state:
    st.session_state.percentage_smartphone = None

if "num_data_card" not in st.session_state:
    st.session_state.num_data_card = None

if "num_smartphone" not in st.session_state:
    st.session_state.num_smartphone = None

total_subscribers = st.number_input("Nombre total d'abonnés", min_value=0, step=1, value=st.session_state.total_subscribers)
percentage_data_card = st.number_input("Pourcentage Data Card", min_value=0, max_value=100, value=st.session_state.percentage_data_card)
percentage_smartphone = st.number_input("Pourcentage Smartphone", min_value=0, max_value=100, value=st.session_state.percentage_smartphone)

st.session_state.total_subscribers = total_subscribers
st.session_state.percentage_data_card = percentage_data_card
st.session_state.percentage_smartphone = percentage_smartphone

num_data_card = int(total_subscribers * (percentage_data_card / 100)) if percentage_data_card is not None else None
num_smartphone = int(total_subscribers * (percentage_smartphone / 100)) if percentage_smartphone is not None else None

st.session_state.num_data_card = num_data_card
st.session_state.num_smartphone = num_smartphone

data = {
    "Nombre total d'abonnés": [total_subscribers],
    "Nombre de \"Data Card\"": [num_data_card],
    "Nombre de Smartphones": [num_smartphone]
}
df = pd.DataFrame(data)
st.table(df)