import streamlit as st
import pandas as pd

st.set_page_config(page_title="VPN", page_icon="🌐", layout="wide")
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

if "total_internet_dl_phone" not in st.session_state:
    st.session_state.total_internet_dl_phone = 0.0

if "total_internet_dl_card" not in st.session_state:
    st.session_state.total_internet_dl_card = 0.0

if "total_vpn_ul_dl_card" not in st.session_state:
    st.session_state.total_vpn_ul_dl_card = 0.0

if "total_vpn_dl_card" not in st.session_state:
    st.session_state.total_vpn_dl_card = 0.0

if "vpn_via_data_card" not in st.session_state:
    st.session_state.vpn_via_data_card = 0.0

# Etat de session des variables résultantes de calculs :
if "volume_trafic_total_phone" not in st.session_state:
    st.session_state.volume_trafic_total_phone = 0.0

if "volume_trafic_total_card" not in st.session_state:
    st.session_state.volume_trafic_total_card = 0.0

if "volume_trafic_total" not in st.session_state:
    st.session_state.volume_trafic_total = 0.0

if "debit_internet" not in st.session_state:
    st.session_state.debit_internet = 0.0

if "data_card_using_vpn" not in st.session_state:
    st.session_state.data_card_using_vpn = 0.0

if "trafic_total_vpn" not in st.session_state:
    st.session_state.trafic_total_vpn = 0.0

if "debit_total_vpn" not in st.session_state:
    st.session_state.debit_total_vpn = 0.0

if "volume_trafic_total_phone_dl" not in st.session_state:
    st.session_state.volume_trafic_total_phone_dl = 0.0

if "volume_trafic_total_card_dl" not in st.session_state:
    st.session_state.volume_trafic_total_card_dl = 0.0

if "volume_trafic_total_dl" not in st.session_state:
    st.session_state.volume_trafic_total_dl = 0.0

if "debit_internet_dl" not in st.session_state:
    st.session_state.debit_internet_dl = 0.0

if "data_card_using_vpn_dl" not in st.session_state:
    st.session_state.data_card_using_vpn_dl = 0.0

if "trafic_total_vpn_dl" not in st.session_state:
    st.session_state.trafic_total_vpn_dl = 0.0

if "debit_total_vpn_dl" not in st.session_state:
    st.session_state.debit_total_vpn_dl = 0.0

total_subscribers = st.number_input("Nombre total d'abonnés", value=st.session_state.total_subscribers)
percentage_data_card = st.number_input("Pourcentage Data Card", min_value=0.0, max_value=100.0, value=st.session_state.percentage_data_card)
percentage_smartphone = st.number_input("Pourcentage Smartphone", min_value=0.0, max_value=100.0, value=st.session_state.percentage_smartphone)

st.session_state.total_subscribers = total_subscribers
st.session_state.percentage_data_card = percentage_data_card
st.session_state.percentage_smartphone = percentage_smartphone

num_data_card = int(total_subscribers * (percentage_data_card / 100)) if percentage_data_card is not None else None
num_smartphone = int(total_subscribers * (percentage_smartphone / 100)) if percentage_smartphone is not None else None
vpn_via_data_card = st.number_input("VPN (via Data Card) en pourcentage", min_value=0.0, max_value=100.0, value=st.session_state.vpn_via_data_card)

total_subscribers = int(total_subscribers)
st.session_state.num_data_card = num_data_card
st.session_state.num_smartphone = num_smartphone
st.session_state.vpn_via_data_card = vpn_via_data_card

data = {
    "Nombre total d'abonnés": [total_subscribers],
    "Nombre de \"Data Card\"": [num_data_card],
    "Nombre de Smartphones": [num_smartphone]
}
df = pd.DataFrame(data)
st.table(df)

st.markdown(" **:blue[Procédons au calcul maintenant, Appuyez sur le bouton calculer :]**")


total_internet_ul_dl_phone = st.session_state.total_internet_ul_dl_phone 
total_internet_ul_dl_card = st.session_state.total_internet_ul_dl_card 
total_vpn_ul_dl_card = st.session_state.total_vpn_ul_dl_card 
vpn_via_data_card = st.session_state.vpn_via_data_card 

total_internet_dl_phone = st.session_state.total_internet_dl_phone
total_internet_dl_card = st.session_state.total_internet_dl_card
total_vpn_dl_card = st.session_state.total_vpn_dl_card 

# Création des variables aux résultantes de calculs
volume_trafic_total_phone = st.session_state.volume_trafic_total_phone
volume_trafic_total_card = st.session_state.volume_trafic_total_card
volume_trafic_total = st.session_state.volume_trafic_total
debit_internet = st.session_state.debit_internet
data_card_using_vpn = st.session_state.data_card_using_vpn
trafic_total_vpn = st.session_state.trafic_total_vpn
debit_total_vpn = st.session_state.debit_total_vpn
volume_trafic_total_phone_dl = st.session_state.volume_trafic_total_phone_dl
volume_trafic_total_card_dl = st.session_state.volume_trafic_total_card_dl
volume_trafic_total_dl = st.session_state.volume_trafic_total_dl
debit_internet_dl = st.session_state.debit_internet_dl
data_card_using_vpn_dl = st.session_state.data_card_using_vpn_dl
trafic_total_vpn_dl = st.session_state.trafic_total_vpn_dl
debit_total_vpn_dl = st.session_state.debit_total_vpn_dl

if st.button("Calculer"):
    # UL/DL
    volume_trafic_total_phone = total_internet_ul_dl_phone * num_smartphone / 1000000
    volume_trafic_total_card = total_internet_ul_dl_card * num_data_card / 1000000
    volume_trafic_total = volume_trafic_total_phone + volume_trafic_total_card
    debit_internet = volume_trafic_total * 8 * 1000 / 3600
    data_card_using_vpn = num_data_card * (vpn_via_data_card / 100)
    trafic_total_vpn = data_card_using_vpn * total_vpn_ul_dl_card / 1000000
    debit_total_vpn = trafic_total_vpn * 8 * 1000 / 3600

    # DL
    volume_trafic_total_phone_dl = total_internet_dl_phone * num_smartphone / 1000000
    volume_trafic_total_card_dl = total_internet_dl_card * num_data_card / 1000000
    volume_trafic_total_dl = volume_trafic_total_phone_dl + volume_trafic_total_card_dl
    debit_internet_dl = volume_trafic_total_dl * 8 * 1000 / 3600
    data_card_using_vpn_dl = num_data_card * (vpn_via_data_card / 100)
    trafic_total_vpn_dl = data_card_using_vpn_dl * total_vpn_dl_card / 1000000
    debit_total_vpn_dl = trafic_total_vpn_dl * 8 * 1000 / 3600



# Mise à jour des valeurs dans l'état de session :
st.session_state.volume_trafic_total_phone = volume_trafic_total_phone
st.session_state.volume_trafic_total_card = volume_trafic_total_card
st.session_state.volume_trafic_total = volume_trafic_total
st.session_state.debit_internet = debit_internet
st.session_state.data_card_using_vpn = data_card_using_vpn
st.session_state.trafic_total_vpn = trafic_total_vpn
st.session_state.debit_total_vpn = debit_total_vpn
st.session_state.volume_trafic_total_phone_dl = volume_trafic_total_phone_dl
st.session_state.volume_trafic_total_card_dl = volume_trafic_total_card_dl
st.session_state.volume_trafic_total_dl = volume_trafic_total_dl
st.session_state.debit_internet_dl = debit_internet_dl
st.session_state.data_card_using_vpn_dl = data_card_using_vpn_dl
st.session_state.trafic_total_vpn_dl = trafic_total_vpn_dl
st.session_state.debit_total_vpn_dl = debit_total_vpn_dl




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
    "Trafic total à l'HC - DL/UL": [
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


data3 = {
    "Désignation": [
        "Volume trafic total pour tous les smartphones (Gb)",
        "Volume trafic total pour les cartes de données (Gb)",
        "Volume de trafic total (Gb)",
        "Debit Internet a l'HC - DL (Gbits/s)",
        "Data Card (Cartes de donnés) utilisant VPN",
        "Trafic total pour VPN (Gb)",
        "Débit total VPN (data card) (Gbits/s)"
    ],
    "Trafic total à l'HC en DL": [
        volume_trafic_total_phone_dl,
        volume_trafic_total_card_dl,
        volume_trafic_total_dl,
        debit_internet_dl,
        data_card_using_vpn_dl,
        trafic_total_vpn_dl,
        debit_total_vpn_dl
    ]
}

df3 = pd.DataFrame(data3)

# Afficher les dataframes côte à côte
col1, col2 = st.columns(2)
col1.table(df2)
col2.table(df3)