import streamlit as st

st.title("Ingestão de Dados do Airbnb")
name = st.text_input("Responsável pela Ingestão")
date_check_in = st.date_input("Check-in")
date_check_out = st.date_input("Check-out")
location = st.selectbox(label="Localidade", options=["Fortaleza", "Cumbuca", "Beberibe"])
confirm = st.button("Solicitar Ingestão")

if confirm:
  payload = {
    "name": name,
    "check_in": date_check_in,
    "check_out": date_check_out,
    "localizacao": location
  }

  # Envia payload para a lambda
  #############################