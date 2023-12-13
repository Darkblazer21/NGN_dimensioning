import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plan Usager EPC", page_icon="📊", layout="wide")

st.markdown("# Dimensionnement du plan usager de l'EPC 📊")
st.sidebar.markdown("# C'est la quatrième page 🌌")

st.markdown("## Dimensionner le plan usager de l'EPC (données des utilisateurs Smarphones + Data Card)")

if "overhead_per_packet" not in st.session_state:
    st.session_state.overhead_per_packet = 0.0

if "packet_size" not in st.session_state:
    st.session_state.packet_size = 0.0

if "overhead" not in st.session_state:
    st.session_state.overhead = 0.0

if "internet_debit_service" not in st.session_state:
    st.session_state.internet_debit_service = 0.0

if "vpn_debit_service" not in st.session_state:
    st.session_state.vpn_debit_service = 0.0

if "total_debit" not in st.session_state:
    st.session_state.total_debit = 0.0

if "debit_internet_dl" not in st.session_state:
    st.session_state.debit_internet_dl = 0.0

if "debit_total_vpn_dl" not in st.session_state:
    st.session_state.debit_total_vpn_dl = 0.0


# Récupérer les valeurs fournies par l'utilisateur
overhead_per_packet = st.number_input("Overhead par paquet (octets)", value=st.session_state.overhead_per_packet)
packet_size = st.number_input("Taille paquet", value=st.session_state.packet_size)

# Calculer les valeurs des tableaux
overhead = overhead_per_packet * packet_size
internet_debit_service = (1 + overhead) * st.session_state.debit_internet_dl
vpn_debit_service = (1 + overhead) * st.session_state.debit_total_vpn_dl
total_debit = internet_debit_service + vpn_debit_service

# Mettre à jour les valeurs dans l'état de session
st.session_state.overhead_per_packet = overhead_per_packet
st.session_state.packet_size = packet_size
st.session_state.overhead = overhead
st.session_state.internet_debit_service = internet_debit_service
st.session_state.vpn_debit_service = vpn_debit_service
st.session_state.total_debit = total_debit

# Créer les tableaux
columns = ["", "Pour l'interface S1U", "Pour l'interface S5", "Pour l'interface SGi"]
table_data = [
    ["Overhead par paquet (octets)", overhead_per_packet, overhead_per_packet, overhead_per_packet],
    ["Taille paquet", packet_size, packet_size, packet_size],
    ["Overhead", overhead, overhead, overhead],
    ["Débit pour les services Internet", internet_debit_service, internet_debit_service, internet_debit_service],
    ["Débit pour le service VPN", vpn_debit_service, vpn_debit_service, vpn_debit_service],
    ["Débit total", total_debit, total_debit, total_debit]
]

df = pd.DataFrame(table_data, columns=columns)

# Afficher les tableaux côte à côte
col1, col2, col3 = st.columns(3)

with col1:
    st.write(df[["", "Pour l'interface S1U"]])

with col2:
    st.write(df[["", "Pour l'interface S5"]])

with col3:
    st.write(df[["", "Pour l'interface SGi"]])
