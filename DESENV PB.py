import streamlit as st;

with st.form(key="include_cliente"):
    input_nome = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sua idade")
    input_occupation = st.selectbox("Selecione seu curso",["Ed.Fisica", "Nutriçao", "Ads", "Direito"])
    input_button_submit = st.form_submit_button("Enviar")

