import streamlit as st

st.set_page_config(page_title="Accueil", page_icon="👋", layout="centered")

st.markdown("# Bienvenue sur l'application de dimensionnement EPC de Brems MBODJ 👨‍💻⚡️🚀")
st.write("\n")
st.sidebar.markdown("# Page d'accueil 🤓")

st.header(":orange[Objectif de l'application :]")
st.markdown('''
:white[**L'outil de dimensionnement EPC mis en place permet de :**]
''')
multi = ''' 
- ✔️ :blue[déterminer le volume de trafic Internet & VPN généré par une "Data Card"  en UL/DL et DL]     
- ✔️ :blue[déterminer le volume de trafic Internet généré par un  smartphone LTE en UL/DL et DL]
- ✔️ :blue[déterminer le trafic total pour VPN et Internet à l'Heure Chargée en Downlink et Uplink]
- ✔️ :blue[dimensionner le plan usager de l'EPC (données des utilisateurs Smarphones + Data Card)]
- ✔️ :blue[dimensionner le plan de contrôle de l'EPC]
- ✔️ :blue[calculer le nombre total d'opérations pour chaque procédure de signalisation]
- ✔️ :blue[dimensionner les différents nœuds EPC]
- ✔️ :blue[déterminer le nombre de nœuds requis] '''
st.markdown(multi)