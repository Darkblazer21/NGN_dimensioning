import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plan de contrôle", page_icon="🗺️", layout="wide")
st.markdown("# Dimensionnement du Plan de Contrôle 🗺️")
st.sidebar.markdown("# C'est la sixième page 🛸")

if "mean_msg_size" not in st.session_state:
    st.session_state.mean_msg_size = 0.0

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

variables = {
    "msg_count_attach": 0.0,
    "msg_count_detach": 0.0,
    "msg_count_idle": 0.0,
    "msg_count_pdn": 0.0,
    "msg_count_bearers": 0.0,
    "msg_count_tau_inter_mme": 0.0,
    "msg_count_tau": 0.0,
    "msg_count_x2_ho": 0.0,
    "msg_count_s1_ho": 0.0,
    "msg_count_ho_inter_mme": 0.0

}

variables1 = {
    "msg_count_attach_s11": 0.0,
    "msg_count_detach_s11": 0.0,
    "msg_count_idle_s11": 0.0,
    "msg_count_pdn_s11": 0.0,
    "msg_count_bearers_s11": 0.0,
    "msg_count_tau_inter_mme_s11": 0.0,
    "msg_count_tau_s11": 0.0,
    "msg_count_x2_ho_s11": 0.0,
    "msg_count_s1_ho_s11": 0.0,
    "msg_count_ho_inter_mme_s11": 0.0

}

variables2 = {
    "msg_count_attach_s8": 0.0,
    "msg_count_detach_s8": 0.0,
    "msg_count_idle_s8": 0.0,
    "msg_count_pdn_s8": 0.0,
    "msg_count_bearers_s8": 0.0,
    "msg_count_tau_inter_mme_s8": 0.0,
    "msg_count_tau_s8": 0.0,
    "msg_count_x2_ho_s8": 0.0,
    "msg_count_s1_ho_s8": 0.0,
    "msg_count_ho_inter_mme_s8": 0.0

}

variables3 = {
    "msg_count_attach_s6a": 0.0,
    "msg_count_detach_s6a": 0.0,
    "msg_count_idle_s6a": 0.0,
    "msg_count_pdn_s6a": 0.0,
    "msg_count_bearers_s6a": 0.0,
    "msg_count_tau_inter_mme_s6a": 0.0,
    "msg_count_tau_s6a": 0.0,
    "msg_count_x2_ho_s6a": 0.0,
    "msg_count_s1_ho_s6a": 0.0,
    "msg_count_ho_inter_mme_s6a": 0.0

}

capacity_s1 = {
    "attach_s1": 0.0,
    "detach_s1": 0.0,
    "idle_s1": 0.0,
    "pdn_s1": 0.0,
    "bearers_s1": 0.0,
    "tau_int_s1": 0.0,
    "tau_s1": 0.0,
    "x2_ho_s1": 0.0,
    "s1_ho_s1": 0.0,
    "ho_int_s1": 0.0
}


capacity_s11 = {
    "attach_s11": 0.0,
    "detach_s11": 0.0,
    "idle_s11": 0.0,
    "pdn_s11": 0.0,
    "bearers_s11": 0.0,
    "tau_int_s11": 0.0,
    "tau_s11": 0.0,
    "x2_ho_s11": 0.0,
    "s1_ho_s11": 0.0,
    "ho_int_s11": 0.0
}

capacity_s8 = {
    "attach_s8": 0.0,
    "detach_s8": 0.0,
    "idle_s8": 0.0,
    "pdn_s8": 0.0,
    "bearers_s8": 0.0,
    "tau_int_s8": 0.0,
    "tau_s8": 0.0,
    "x2_ho_s8": 0.0,
    "s1_ho_s8": 0.0,
    "ho_int_s8": 0.0
}

capacity_s6a = {
    "attach_s6a": 0.0,
    "detach_s6a": 0.0,
    "idle_s6a": 0.0,
    "pdn_s6a": 0.0,
    "bearers_s6a": 0.0,
    "tau_int_s6a": 0.0,
    "tau_s6a": 0.0,
    "x2_ho_s6a": 0.0,
    "s1_ho_s6a": 0.0,
    "ho_int_s6a": 0.0
}


for variable, value in variables.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in variables1.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in variables2.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in variables3.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in capacity_s1.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in capacity_s11.items():
    if variable not in st.session_state:
        st.session_state[variable] = value

for variable, value in capacity_s8.items():
    if variable not in st.session_state:
        st.session_state[variable] = value


st.markdown(":green[Veuillez renseigner les informations suivantes avant de commencer :]")
mean_msg_size = st.number_input("Taille moyen d'un message (bits)")

st.session_state.mean_msg_size = mean_msg_size

attach_result = st.session_state.attach_result
detach_result = st.session_state.detach_result
idle_to_active_result = st.session_state.idle_to_active_result
pdn_result = st.session_state.pdn_result
bearers_result = st.session_state.bearers_result
tau_inter_mme_result = st.session_state.tau_inter_mme_result
tau_result = st.session_state.tau_result
x2_ho_result = st.session_state.x2_ho_result
s1_ho_result = st.session_state.s1_ho_result
ho_inter_mme_result = st.session_state.ho_inter_mme_result

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.text("Nombre de messages/procédures")
    for variable in variables:
        st.session_state[variable] = st.number_input(f"{variable}:", value=st.session_state[variable])

with col2:
    st.text("Nombre de messages via s11")
    for variable in variables1:
        st.session_state[variable] = st.number_input(f"{variable}:", value=st.session_state[variable])

with col3:
    st.text("Nombre de messages via S8")
    for variable in variables2:
        st.session_state[variable] = st.number_input(f"{variable}:", value=st.session_state[variable])

with col4:
    st.text("Nombre de messages via S6a")
    for variable in variables3:
        st.session_state[variable] = st.number_input(f"{variable}:", value=st.session_state[variable])


attach_s1 = (mean_msg_size*st.session_state.msg_count_attach*attach_result) / (3600*1000000)
detach_s1 = (mean_msg_size*st.session_state.msg_count_detach*detach_result) / (3600*1000000)
idle_s1 = (mean_msg_size*st.session_state.msg_count_idle*idle_to_active_result) / (3600*1000000)
pdn_s1 = (mean_msg_size*st.session_state.msg_count_pdn*pdn_result) / (3600*1000000)
bearers_s1 = (mean_msg_size*st.session_state.msg_count_bearers*bearers_result) / (3600*1000000)
tau_int_s1 = (mean_msg_size*st.session_state.msg_count_tau_inter_mme*tau_inter_mme_result) / (3600*1000000)
tau_s1 = (mean_msg_size*st.session_state.msg_count_tau*tau_result) / (3600*1000000)
x2_ho_s1 = (mean_msg_size*st.session_state.msg_count_x2_ho*x2_ho_result) / (3600*1000000)
s1_ho_s1 = (mean_msg_size*st.session_state.msg_count_s1_ho*s1_ho_result) / (3600*1000000)
ho_int_s1 = (mean_msg_size*st.session_state.msg_count_ho_inter_mme*ho_inter_mme_result) / (3600*1000000)


st.session_state.attach_s1 = attach_s1
st.session_state.detach_s1 = detach_s1
st.session_state.idle_s1 = idle_s1
st.session_state.pdn_s1 = pdn_s1
st.session_state.bearers_s1 = bearers_s1
st.session_state.tau_int_s1 = tau_int_s1
st.session_state.tau_s1 = tau_s1
st.session_state.x2_ho_s1 = x2_ho_s1
st.session_state.s1_ho_s1 = s1_ho_s1
st.session_state.ho_int_s1 = ho_int_s1


attach_s11 = (mean_msg_size*st.session_state.msg_count_attach_s11*attach_result) / (3600*1000000)
detach_s11 = (mean_msg_size*st.session_state.msg_count_detach_s11*detach_result) / (3600*1000000)
idle_s11 = (mean_msg_size*st.session_state.msg_count_idle_s11*idle_to_active_result) / (3600*1000000)
pdn_s11 = (mean_msg_size*st.session_state.msg_count_pdn_s11*pdn_result) / (3600*1000000)
bearers_s11 = (mean_msg_size*st.session_state.msg_count_bearers_s11*bearers_result) / (3600*1000000)
tau_int_s11 = (mean_msg_size*st.session_state.msg_count_tau_inter_mme_s11*tau_inter_mme_result) / (3600*1000000)
tau_s11 = (mean_msg_size*st.session_state.msg_count_tau_s11*tau_result) / (3600*1000000)
x2_ho_s11 = (mean_msg_size*st.session_state.msg_count_x2_ho_s11*x2_ho_result) / (3600*1000000)
s1_ho_s11 = (mean_msg_size*st.session_state.msg_count_s1_ho_s11*s1_ho_result) / (3600*1000000)
ho_int_s11 = (mean_msg_size*st.session_state.msg_count_ho_inter_mme_s11*ho_inter_mme_result) / (3600*1000000)


st.session_state.attach_s11 = attach_s11
st.session_state.detach_s11 = detach_s11
st.session_state.idle_s11 = idle_s11
st.session_state.pdn_s11 = pdn_s11
st.session_state.bearers_s11 = bearers_s11
st.session_state.tau_int_s11 = tau_int_s11
st.session_state.tau_s11 = tau_s11
st.session_state.x2_ho_s11 = x2_ho_s11
st.session_state.s1_ho_s11 = s1_ho_s11
st.session_state.ho_int_s11 = ho_int_s11


attach_s8 = (mean_msg_size*st.session_state.msg_count_attach_s8*attach_result) / (3600*1000000)
detach_s8 = (mean_msg_size*st.session_state.msg_count_detach_s8*detach_result) / (3600*1000000)
idle_s8 = (mean_msg_size*st.session_state.msg_count_idle_s8*idle_to_active_result) / (3600*1000000)
pdn_s8 = (mean_msg_size*st.session_state.msg_count_pdn_s8*pdn_result) / (3600*1000000)
bearers_s8 = (mean_msg_size*st.session_state.msg_count_bearers_s8*bearers_result) / (3600*1000000)
tau_int_s8 = (mean_msg_size*st.session_state.msg_count_tau_inter_mme_s8*tau_inter_mme_result) / (3600*1000000)
tau_s8 = (mean_msg_size*st.session_state.msg_count_tau_s8*tau_result) / (3600*1000000)
x2_ho_s8 = (mean_msg_size*st.session_state.msg_count_x2_ho_s8*x2_ho_result) / (3600*1000000)
s1_ho_s8 = (mean_msg_size*st.session_state.msg_count_s1_ho_s8*s1_ho_result) / (3600*1000000)
ho_int_s8 = (mean_msg_size*st.session_state.msg_count_ho_inter_mme_s8*ho_inter_mme_result) / (3600*1000000)


st.session_state.attach_s8 = attach_s8
st.session_state.detach_s8 = detach_s8
st.session_state.idle_s8 = idle_s8
st.session_state.pdn_s8 = pdn_s8
st.session_state.bearers_s8 = bearers_s8
st.session_state.tau_int_s8 = tau_int_s8
st.session_state.tau_s8 = tau_s8
st.session_state.x2_ho_s8 = x2_ho_s8
st.session_state.s1_ho_s8 = s1_ho_s8
st.session_state.ho_int_s8 = ho_int_s8


attach_s6a = (mean_msg_size*st.session_state.msg_count_attach_s6a*attach_result) / (3600*1000000)
detach_s6a = (mean_msg_size*st.session_state.msg_count_detach_s6a*detach_result) / (3600*1000000)
idle_s6a = (mean_msg_size*st.session_state.msg_count_idle_s6a*idle_to_active_result) / (3600*1000000)
pdn_s6a = (mean_msg_size*st.session_state.msg_count_pdn_s6a*pdn_result) / (3600*1000000)
bearers_s6a = (mean_msg_size*st.session_state.msg_count_bearers_s6a*bearers_result) / (3600*1000000)
tau_int_s6a = (mean_msg_size*st.session_state.msg_count_tau_inter_mme_s6a*tau_inter_mme_result) / (3600*1000000)
tau_s6a = (mean_msg_size*st.session_state.msg_count_tau_s6a*tau_result) / (3600*1000000)
x2_ho_s6a = (mean_msg_size*st.session_state.msg_count_x2_ho_s6a*x2_ho_result) / (3600*1000000)
s1_ho_s6a = (mean_msg_size*st.session_state.msg_count_s1_ho_s6a*s1_ho_result) / (3600*1000000)
ho_int_s6a = (mean_msg_size*st.session_state.msg_count_ho_inter_mme_s6a*ho_inter_mme_result) / (3600*1000000)


st.session_state.attach_s6a = attach_s6a
st.session_state.detach_s6a = detach_s6a
st.session_state.idle_s6a = idle_s6a
st.session_state.pdn_s6a = pdn_s6a
st.session_state.bearers_s6a = bearers_s6a
st.session_state.tau_int_s6a = tau_int_s6a
st.session_state.tau_s6a = tau_s6a
st.session_state.x2_ho_s6a = x2_ho_s6a
st.session_state.s1_ho_s6a = s1_ho_s6a
st.session_state.ho_int_s6a = ho_int_s6a


columns = ["", "Capacité S1-C (Gbits/s)", "Capacité S11 (Gbits/s)", "Capacité S8 (Gbits/s)", "Capacité S6a (Gbits/s)"]

data = [
    ["N(attach)", attach_s1, attach_s11, attach_s8, attach_s6a],
    ["N(detach)", detach_s1, detach_s11, detach_s8, detach_s6a],
    ["N(idle to active)", idle_s1, idle_s11, idle_s8, idle_s6a],
    ["N(connexions PDN)", pdn_s1, pdn_s11, pdn_s8, pdn_s6a],
    ["N(bearers activ/desactiv)", bearers_s1, bearers_s11, bearers_s8, bearers_s6a],
    ["N(TAU_inter_MME)", tau_int_s1, tau_int_s11, tau_int_s8, tau_int_s6a],
    ["N(TAU_inter_MME/SGW)", tau_s1, tau_s11, tau_s8, tau_s6a],
    ["N(X2_HO)", x2_ho_s1, x2_ho_s11, x2_ho_s8, x2_ho_s6a],
    ["N(S1_HO)", s1_ho_s1, s1_ho_s11, s1_ho_s8, s1_ho_s6a],
    ["N(HO_inter_MME)", ho_int_s1, ho_int_s11, ho_int_s8, ho_int_s6a]
]

# Ajout de la ligne de la capacité totale
numeric_data = [row[1:] for row in data]
total_capacity = ["Capacité totale(Gbits/s)"] + [sum(filter(lambda x: isinstance(x, (int, float)), col)) for col in zip(*numeric_data)]

data.append(total_capacity)

df = pd.DataFrame(data, columns=columns)
st.dataframe(df)

st.write(mean_msg_size)