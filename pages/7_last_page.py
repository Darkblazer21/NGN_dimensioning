import streamlit as st
import pandas as pd

st.set_page_config(page_title="Noeuds EPC", page_icon="🆖", layout="wide")
st.markdown("# :rainbow[Dimensionnement des noeuds EPC et Calcul du nombre de noeuds requis] 💻⚙️🔗")
st.sidebar.markdown("# C'est la dernière page 🥳")

# Variables temporaires pour les calculs avec valeurs par défaut
if 'N_MME_SAU' not in st.session_state:
    st.session_state['N_MME_SAU'] = 6
N_MME_SAU = st.session_state['N_MME_SAU']

if 'N_MME_IDLE_ACTIVE' not in st.session_state:
    st.session_state['N_MME_IDLE_ACTIVE'] = 12
N_MME_IDLE_ACTIVE = st.session_state['N_MME_IDLE_ACTIVE']

if 'N_MME_TRANS_SECOND' not in st.session_state:
    st.session_state['N_MME_TRANS_SECOND'] = 11
N_MME_TRANS_SECOND = st.session_state['N_MME_TRANS_SECOND']

if 'N_SGW_BEARERS' not in st.session_state:
    st.session_state['N_SGW_BEARERS'] = 2
N_SGW_BEARERS = st.session_state['N_SGW_BEARERS']

if 'N_SGW_BH_DL_INTERNET' not in st.session_state:
    st.session_state['N_SGW_BH_DL_INTERNET'] = 5
N_SGW_BH_DL_INTERNET = st.session_state['N_SGW_BH_DL_INTERNET']

if 'N_SGW_BH_DL_VPN' not in st.session_state:
    st.session_state['N_SGW_BH_DL_VPN'] = 1
N_SGW_BH_DL_VPN = st.session_state['N_SGW_BH_DL_VPN']

if 'N_PGW_BEARERS' not in st.session_state:
    st.session_state['N_PGW_BEARERS'] = 2
N_PGW_BEARERS = st.session_state['N_PGW_BEARERS']

if 'N_PGW_BH_DL_INTERNET' not in st.session_state:
    st.session_state['N_PGW_BH_DL_INTERNET'] = 5
N_PGW_BH_DL_INTERNET = st.session_state['N_PGW_BH_DL_INTERNET']

if 'N_PGW_BH_DL_VPN' not in st.session_state:
    st.session_state['N_PGW_BH_DL_VPN'] = 1
N_PGW_BH_DL_VPN = st.session_state['N_PGW_BH_DL_VPN']

if 'N_SGW_PGW_BEARERS' not in st.session_state:
    st.session_state['N_SGW_PGW_BEARERS'] = 2
N_SGW_PGW_BEARERS = st.session_state['N_SGW_PGW_BEARERS']

if 'N_SGW_PGW_BH_DL_INTERNET' not in st.session_state:
    st.session_state['N_SGW_PGW_BH_DL_INTERNET'] = 10
N_SGW_PGW_BH_DL_INTERNET = st.session_state['N_SGW_PGW_BH_DL_INTERNET']

if 'N_SGW_PGW_BH_DL_VPN' not in st.session_state:
    st.session_state['N_SGW_PGW_BH_DL_VPN'] = 1
N_SGW_PGW_BH_DL_VPN = st.session_state['N_SGW_PGW_BH_DL_VPN']

if 'N_HSS' not in st.session_state:
    st.session_state['N_HSS'] = 1
N_HSS = st.session_state['N_HSS']

if 'N_PCRF' not in st.session_state:
    st.session_state['N_PCRF'] = 20
N_PCRF = st.session_state['N_PCRF']


# Vérifier si les valeurs sont déjà enregistrées dans l'état de session
if 'valeurs' not in st.session_state:
    st.session_state['valeurs'] = {}

# Création du DataFrame initial
data = {
    'Composants': ['MME', '', '', 'SGW', '', 'PGW', '', 'SGW/PGW Combiné', '', 'HSS', 'PCRF'],
    'Metriques': ['Simultaneous Attached Users(SAU)', 'Transitions idle/active par seconde', 'Nbre total transactions par seconde', 'Nombre de bearers', 'Capacité traitement de données', 'Nombre de bearers', 'Capacité traitement de données', 'Nombre de bearers', 'Capacité traitement de données', 'Nombre d\'abonnés supportés', 'Nbre total transactions par seconde'],
    'Unité': ['abonnés', 'transitions/seconde', 'transactions/seconde', 'bearers', 'Gbits', 'bearers', 'Gbits', 'bearers', 'Gbits', 'abonnés', 'transactions/seconde'],
    'Valeur': ['', '', '', '', '', '', '', '', '', '', ''],
    'Pourcentage': ['', '', '', '', '', '', '', '', '', '', ''],
    'Capacité d\'exploitation': ['', '', '', '', '', '', '', '', '', '', '']
}
df = pd.DataFrame(data)

# Afficher le DataFrame initial
st.subheader("Dimensionnement des nœuds LTE")
st.subheader("Valeurs préliminaires")
st.markdown(":blue[**Veuillez renseigner les valeurs et les pourcentages dans les champs suivants:**]")


# Saisie des valeurs par l'utilisateur
for i, row in df.iterrows():
    if row['Unité'] != '':
        composant = row['Unité']
        col1, col2 = st.columns(2)
        with col1:
            valeur = st.text_input(f"Valeur pour '{composant}'", key=f"valeur_{i}", value=st.session_state['valeurs'].get(f"valeur_{i}", ''))
            st.session_state['valeurs'][f"valeur_{i}"] = valeur
        with col2:
            pourcentage = st.text_input(f"Pourcentage pour '{composant}'", key=f"pourcentage_{i}", value=st.session_state['valeurs'].get(f"pourcentage_{i}", ''))
            st.session_state['valeurs'][f"pourcentage_{i}"] = pourcentage

# Calcul des valeurs de la colonne 'Capacité d'exploitation'
for i, row in df.iterrows():
    if row['Unité'] != '':
        valeur = st.session_state['valeurs'].get(f"valeur_{i}", '')
        pourcentage = st.session_state['valeurs'].get(f"pourcentage_{i}", '')

        if valeur != '' and pourcentage != '':
            df.at[i, "Valeur"] = valeur
            df.at[i, "Pourcentage"] = pourcentage
            capacite_exploitation = str(float(valeur) * (float(pourcentage.strip('%')) / 100))
            df.at[i, "Capacité d'exploitation"] = capacite_exploitation + ' ' + row['Unité']

# Afficher le DataFrame mis à jour
st.subheader("DataFrame mis à jour")
st.dataframe(df)