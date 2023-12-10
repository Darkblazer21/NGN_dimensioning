import streamlit as st
import pandas as pd

st.set_page_config(page_title="VPN", page_icon="🌐", layout="centered")
st.markdown("# :rainbow[Les VPN c'est comme des ninjas] 🐱‍👤")
st.sidebar.markdown("# C'est la troisième page 🎭")
st.markdown("## Trafic total pour VPN et Internet à l'Heure Chargée en Downlink et Uplink")

st.markdown(":green[**Avant de commencer nous avons besoin de certaines infos :**]")

# Initialiser l'état de la session pour cette page
if "total_subscribers" not in st.session_state:
    st.session_state.total_subscribers = 0.0

if "percentage_data_card" not in st.session_state:
    st.session_state.percentage_data_card = 0.0

if "percentage_smartphone" not in st.session_state:
    st.session_state.percentage_smartphone = 0.0

if "num_data_card" not in st.session_state:
    st.session_state.num_data_card = 0.0

if "num_smartphone" not in st.session_state:
    st.session_state.num_smartphone = 0.0

if "total_internet_ul_dl_phone" not in st.session_state:
    st.session_state.total_internet_ul_dl_phone = 0.0

if "total_internet_ul_dl_card" not in st.session_state:
    st.session_state.total_internet_ul_dl_card = 0.0

if "total_vpn_ul_dl_card" not in st.session_state:
    st.session_state.total_vpn_ul_dl_card = 0.0

if "vpn_via_data_card" not in st.session_state:
    st.session_state.vpn_via_data_card = 0.0

total_subscribers = st.number_input("Nombre total d'abonnés", min_value=0.0, step=1.0, value=st.session_state.total_subscribers)
percentage_data_card = st.number_input("Pourcentage Data Card", min_value=0.0, max_value=100.0, value=st.session_state.percentage_data_card)
percentage_smartphone = st.number_input("Pourcentage Smartphone", min_value=0.0, max_value=100.0, value=st.session_state.percentage_smartphone)

st.session_state.total_subscribers = total_subscribers
st.session_state.percentage_data_card = percentage_data_card
st.session_state.percentage_smartphone = percentage_smartphone

num_data_card = int(total_subscribers * (percentage_data_card / 100)) if percentage_data_card is not None else None
num_smartphone = int(total_subscribers * (percentage_smartphone / 100)) if percentage_smartphone is not None else None

total_subscribers = int(total_subscribers)
st.session_state.num_data_card = num_data_card
st.session_state.num_smartphone = num_smartphone

data = {
    "Nombre total d'abonnés": [total_subscribers],
    "Nombre de \"Data Card\"": [num_data_card],
    "Nombre de Smartphones": [num_smartphone]
}
df = pd.DataFrame(data)
st.table(df)

st.markdown(" **:blue[Procédons au calcul maintenant, remplis les champs suivants :]**")

# Demander à l'utilisateur de saisir les valeurs
total_internet_ul_dl_phone = st.number_input("Total trafic Internet en UL/DL pour les Smartphones", value=st.session_state.total_internet_ul_dl_phone)
total_internet_ul_dl_card = st.number_input("Total trafic Internet en UL/DL pour les Data cards", value=st.session_state.total_internet_dl_card)
total_vpn_ul_dl_card = st.number_input("Total trafic VPN en UL/DL pour les Data Card", value=st.session_state.total_vpn_ul_dl_card)
vpn_via_data_card = st.number_input("VPN (via Data Card) en pourcentage", min_value=0.0, max_value=100.0, value=st.session_state.vpn_via_data_card)


st.session_state.total_internet_ul_dl_phone = total_internet_ul_dl_phone
st.session_state.total_internet_ul_dl_card = total_internet_ul_dl_card
st.session_state.total_vpn_ul_dl_card = total_vpn_ul_dl_card
st.session_state.vpn_via_data_card = vpn_via_data_card

volume_trafic_total_phone = 0.0
volume_trafic_total_card = 0.0
volume_trafic_total = 0.0
debit_internet = 0.0
data_card_using_vpn = 0.0
trafic_total_vpn = 0.0
debit_total_vpn = 0.0

if st.button("Calculer"):
    volume_trafic_total_phone = total_internet_ul_dl_phone * num_smartphone / 1000000
    volume_trafic_total_card = total_internet_ul_dl_card * num_data_card / 1000000
    volume_trafic_total = volume_trafic_total_phone + volume_trafic_total_card
    debit_internet = volume_trafic_total * 8 * 1000 / 3600
    data_card_using_vpn = num_data_card * (vpn_via_data_card / 100)
    trafic_total_vpn = data_card_using_vpn * total_vpn_ul_dl_card / 1000000
    debit_total_vpn = trafic_total_vpn * 8 * 1000 / 3600


# Afficher le tableau des résultats
data2 = {
    "Désignation": [
        "Volume trafic total pour tous les smartphones (Gb)",
        "Volume trafic total pour les cartes de données (Gb)",
        "Volume de trafic total (Gb)",
        "Debit Internet a l'HC - UL/DL  (Gbits/s)",
        "Data Card (Cartes de donnés) utilisant VPN",
        "Trafic total pour VPN (Gb)",
        "Débit total VPN (data card) (Gbits/s)"
    ],
    "Trafic total à l'HC - DL/HL": [
        volume_trafic_total_phone,
        volume_trafic_total_card,
        volume_trafic_total,
        debit_internet,
        data_card_using_vpn,
        trafic_total_vpn,
        debit_total_vpn
    ]
}
df2 = pd.DataFrame(data2)
st.table(df2)
