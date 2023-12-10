import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smartphone", page_icon="📱", layout="centered")

st.markdown("# Voyons le calcul pour les smartphones 🤔🤳🏽")
st.sidebar.markdown("# C'est la deuxième page ✨")

st.markdown("## Volume de trafic Internet & VPN généré par un \"Smartphone\" en UL/DL et DL")

# Initialiser l'état de la session avec un dataframe vide
if "data_page2" not in st.session_state:
    st.session_state.data_page2 = pd.DataFrame(columns=['Type de services', 'Nombre de session à l\'HC', 'Taille session à l\'HC', 'Pourcentage DL', 'Volume trafic à l\'HC en UL/DL (Mb)', 'Volume trafic à l\'HC en DL (Mb)'])

if "total_internet_ul_dl_phone" not in st.session_state:
    st.session_state.total_internet_ul_dl_phone = 0.0

if "total_internet_dl_phone" not in st.session_state:
    st.session_state.total_internet_dl_phone = 0.0



services = ['Navigation web', 'Email', 'Streaming video', 'VPN', 'Gaming']

if st.session_state.data_page2.empty:
    for i, service in enumerate(services):
        st.session_state.data_page2.loc[i] = [service, None, None, None, None, None]

with st.form(key='my_form'):
    for index, row in st.session_state.data_page2.iterrows():
        st.write(row['Type de services'])
        session = st.number_input('Nombre de session à l\'HC', key=f"session_{index}", value=row['Nombre de session à l\'HC'] or 0.0)
        taille = st.number_input('Taille session à l\'HC', key=f"taille_{index}", value=row['Taille session à l\'HC'] or 0.0)
        pourcentage = st.number_input('Pourcentage DL', min_value=0.0, max_value=100.0, key=f"pourcentage_{index}", value=row['Pourcentage DL'] or 0.0)
        st.session_state.data_page2.at[index, 'Nombre de session à l\'HC'] = session
        st.session_state.data_page2.at[index, 'Taille session à l\'HC'] = taille
        st.session_state.data_page2.at[index, 'Pourcentage DL'] = pourcentage
        st.write('---')

    submit_button = st.form_submit_button(label='Calculer')

if submit_button:
    # Réinitialisez les valeurs supplémentaires à zéro
    st.session_state.total_internet_ul_dl_phone = 0.0
    st.session_state.total_internet_dl_phone = 0.0

    for index, row in st.session_state.data_page2.iterrows():
        volume_ul_dl_phone = row['Volume trafic à l\'HC en UL/DL (Mb)']
        volume_dl_phone = row['Volume trafic à l\'HC en DL (Mb)']
        service = row['Type de services']

        if service != 'VPN':
            if volume_ul_dl_phone is not None:
                st.session_state.total_internet_ul_dl_phone += volume_ul_dl_phone
            if volume_dl_phone is not None:
                st.session_state.total_internet_dl_phone += volume_dl_phone


    st.session_state.data_page2['Volume trafic à l\'HC en UL/DL (Mb)'] = st.session_state.data_page2['Taille session à l\'HC'] * st.session_state.data_page2['Nombre de session à l\'HC']
    st.session_state.data_page2['Volume trafic à l\'HC en DL (Mb)'] = st.session_state.data_page2['Volume trafic à l\'HC en UL/DL (Mb)'] * (st.session_state.data_page2['Pourcentage DL'] / 100)

st.table(st.session_state.data_page2)

# Affichage des valeurs supplémentaires
st.markdown("## Volume total du trafic Internet")
st.write(f"- UL/DL : {st.session_state.total_internet_ul_dl_phone} Mb")
st.write(f"- DL : {st.session_state.total_internet_dl_phone} Mb")
