import streamlit as st
import pandas as pd

st.markdown("# 👋 Ici Kingbrems 👑😎")
st.sidebar.markdown("# C'est la première page 🌟")

st.markdown("## Volume de trafic Internet & VPN généré par une \"Data Card\" en UL/DL et DL")

data = pd.DataFrame(columns=['Type de services', 'Nombre de session à l\'HC', 'Taille session à l\'HC', 'Pourcentage DL', 'Volume trafic à l\'HC en UL/DL (Mb)', 'Volume trafic à l\'HC en DL (Mb)'])

services = ['Navigation web', 'Email', 'Streaming video', 'VPN', 'Gaming']
for i, service in enumerate(services):
    data.loc[i] = [service, None, None, None, None, None]

with st.form(key='my_form'):
    for index, row in data.iterrows():
        st.write(row['Type de services'])
        session = st.number_input('Nombre de session à l\'HC', step=1, key=f"session_{index}")
        taille = st.number_input('Taille session à l\'HC', step=1, key=f"taille_{index}")
        pourcentage = st.number_input('Pourcentage DL', min_value=0.0, max_value=100.0, step=1.0, key=f"pourcentage_{index}")
        data.at[index, 'Nombre de session à l\'HC'] = session
        data.at[index, 'Taille session à l\'HC'] = taille
        data.at[index, 'Pourcentage DL'] = pourcentage
        st.write('---')

    submit_button = st.form_submit_button(label='Calculer')

if submit_button:
    data['Volume trafic à l\'HC en UL/DL (Mb)'] = data['Taille session à l\'HC'] * data['Nombre de session à l\'HC']
    data['Volume trafic à l\'HC en DL (Mb)'] = data['Volume trafic à l\'HC en UL/DL (Mb)'] * (data['Pourcentage DL'] / 100)

st.table(data)
