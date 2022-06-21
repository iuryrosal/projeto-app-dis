import streamlit as st
from sqs_service import SQSService
import os
import json

sqs = SQSService()
sqs_url = 'http://localhost:4566/000000000000/sqs_requisicoes'

st.title("Ingestão de Dados do Airbnb")
name = st.text_input("Responsável pela Ingestão")
date_check_in = st.date_input("Check-in")
date_check_out = st.date_input("Check-out")
location = st.selectbox(label="Localidade", options=["Fortaleza", "Cumbuca", "Beberibe"])
confirm = st.button("Solicitar Ingestão")

if confirm:
  payload = json.dumps({
    "name": name,
    "check_in": str(date_check_in),
    "check_out": str(date_check_out),
    "localizacao": location
  })

  # Envia payload para a lambda
  sqs.send_message(sqs_url, payload)