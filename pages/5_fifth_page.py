import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trafic Signalisation", page_icon="📈", layout="centered")

st.markdown("# Calcul du trafic de signalisation 📈")
st.sidebar.markdown("# C'est la cinquième page 🌠")

st.markdown("## Calcul du nombre total d'opérations pour chaque procédure de signalisation")

# Vérifier et initialiser les variables dans l'état de session
if "total_subscribers" not in st.session_state:
    st.session_state.total_subscribers = 0

if "active_subscribers_percentage" not in st.session_state:
    st.session_state.active_subscribers_percentage = 0.0

if "attach_count" not in st.session_state:
    st.session_state.attach_count = 0.0

if "detach_count" not in st.session_state:
    st.session_state.detach_count = 0.0

if "idle_to_active_count" not in st.session_state:
    st.session_state.idle_to_active_count = 0.0

if "pdn_count" not in st.session_state:
    st.session_state.pdn_count = 0.0

if "bearers_count" not in st.session_state:
    st.session_state.bearers_count = 0.0

if "tau_inter_mme_count" not in st.session_state:
    st.session_state.tau_inter_mme_count = 0.0

if "tau_count" not in st.session_state:
    st.session_state.tau_count = 0.0

if "x2_ho_count" not in st.session_state:
    st.session_state.x2_ho_count = 0.0

if "s1_ho_count" not in st.session_state:
    st.session_state.s1_ho_count = 0.0

if "ho_inter_mme_count" not in st.session_state:
    st.session_state.ho_inter_mme_count = 0.0

# Vérifier et initialiser les variables dans l'état de session
if "attach_result" not in st.session_state:
    st.session_state.attach_result = 0.0

if "detach_result" not in st.session_state:
    st.session_state.detach_result = 0.0

if "idle_to_active_result" not in st.session_state:
    st.session_state.idle_to_active_result = 0.0

if "pdn_result" not in st.session_state:
    st.session_state.pdn_result = 0.0

if "bearers_result" not in st.session_state:
    st.session_state.bearers_result = 0.0

if "tau_inter_mme_result" not in st.session_state:
    st.session_state.tau_inter_mme_result = 0.0

if "tau_result" not in st.session_state:
    st.session_state.tau_result = 0.0

if "x2_ho_result" not in st.session_state:
    st.session_state.x2_ho_result = 0.0

if "s1_ho_result" not in st.session_state:
    st.session_state.s1_ho_result = 0.0

if "ho_inter_mme_result" not in st.session_state:
    st.session_state.ho_inter_mme_result = 0.0

if "total_procedures" not in st.session_state:
    st.session_state.total_procedures = 0.0

# Récupérer le pourcentage d'utilisateurs actifs à l'HC donné par l'utilisateur
active_subscribers_percentage = st.number_input("Pourcentage d'utilisateurs actifs à l'HC", min_value=0.0, max_value=100.0, value=st.session_state.active_subscribers_percentage)

# Calculer le nombre d'abonnés actifs à l'HC
active_subscribers_count = st.session_state.total_subscribers * (active_subscribers_percentage / 100)

# Mettre à jour les valeurs dans l'état de session
st.session_state.active_subscribers_percentage = active_subscribers_percentage
st.session_state.active_subscribers_count = active_subscribers_count

# Demander à l'utilisateur de saisir les valeurs pour chaque élément
attach_count = st.number_input("Valeur pour N(attach)", value=st.session_state.attach_count, format="%.2f")
st.session_state.attach_count = attach_count

detach_count = st.number_input("Valeur pour N(detach)", value=st.session_state.detach_count, format="%.2f")
st.session_state.detach_count = detach_count

idle_to_active_count = st.number_input("Valeur pour N(idle to active)", value=st.session_state.idle_to_active_count, format="%.2f")
st.session_state.idle_to_active_count = idle_to_active_count

pdn_count = st.number_input("Valeur pour N(PDN)", value=st.session_state.pdn_count, format="%.2f")
st.session_state.pdn_count = pdn_count

bearers_count = st.number_input("Valeur pour N(bearers activ/desactiv)", value=st.session_state.bearers_count, format="%.2f")
st.session_state.bearers_count = bearers_count

tau_inter_mme_count = st.number_input("Valeur pour N(TAU_inter_MME)", value=st.session_state.tau_inter_mme_count, format="%.2f")
st.session_state.tau_inter_mme_count = tau_inter_mme_count

tau_count = st.number_input("Valeur pour N(TAU)", value=st.session_state.tau_count, format="%.2f")
st.session_state.tau_count = tau_count

x2_ho_count = st.number_input("Valeur pour N(X2_HO)", value=st.session_state.x2_ho_count, format="%.2f")
st.session_state.x2_ho_count = x2_ho_count

s1_ho_count = st.number_input("Valeur pour N(S1_HO)", value=st.session_state.s1_ho_count, format="%.2f")
st.session_state.s1_ho_count = s1_ho_count

ho_inter_mme_count = st.number_input("Valeur pour N(HO_inter_MME)", value=st.session_state.ho_inter_mme_count, format="%.2f")
st.session_state.ho_inter_mme_count = ho_inter_mme_count

# Calculer les résultats en multipliant par le nombre d'abonnés actifs à l'HC
attach_result = attach_count * active_subscribers_count
detach_result = detach_count * active_subscribers_count
idle_to_active_result = idle_to_active_count * active_subscribers_count
pdn_result = pdn_count * active_subscribers_count
bearers_result = bearers_count * active_subscribers_count
tau_inter_mme_result = tau_inter_mme_count * active_subscribers_count
tau_result = tau_count * active_subscribers_count
x2_ho_result = x2_ho_count * active_subscribers_count
s1_ho_result = s1_ho_count * active_subscribers_count
ho_inter_mme_result = ho_inter_mme_count * active_subscribers_count

st.session_state.attach_result = attach_result
st.session_state.detach_result = detach_result
st.session_state.idle_to_active_result = idle_to_active_result
st.session_state.pdn_result = pdn_result
st.session_state.bearers_result = bearers_result
st.session_state.tau_inter_mme_result = tau_inter_mme_result
st.session_state.tau_result = tau_result
st.session_state.x2_ho_result = x2_ho_result
st.session_state.s1_ho_result = s1_ho_result
st.session_state.ho_inter_mme_result = ho_inter_mme_result

columns = ["Données", "Procédure/Abonné/HC", "Nombre"]

# Afficher les résultats sous forme de tableau
results_table = [
    ["N(attach)", attach_count, attach_result],
    ["N(detach)",detach_count, detach_result],
    ["N(idle to active)", idle_to_active_count, idle_to_active_result],
    ["N(PDN)", pdn_count, pdn_result],
    ["N(bearers activ/desactiv)", bearers_count, bearers_result],
    ["N(TAU_inter_MME)", tau_inter_mme_count, tau_inter_mme_result],
    ["N(TAU)", tau_count, tau_result],
    ["N(X2_HO)", x2_ho_count, x2_ho_result],
    ["N(S1_HO)", s1_ho_count, s1_ho_result],
    ["N(HO_inter_MME)", ho_inter_mme_count, ho_inter_mme_result]
]

df = pd.DataFrame(results_table, columns=columns)

st.table(df)

# Calculer la somme des valeurs dans la colonne "Nombre"
total_procedures = df['Nombre'].sum()
st.session_state.total_procedures = total_procedures


# Afficher la valeur "N(procédures)"
st.write(f"N(procédures) : {total_procedures}")