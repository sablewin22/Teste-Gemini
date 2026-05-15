import requests
import streamlit as st
import os
import google.generativeai as genai
# Configura a API Key do Google Gemini e grava em uma variável de ambiente

genai.configure(api_key=st.secrets['GEMINI_API_KEY'])

# Configura o cliente da SDK do Gemini

MODEL_ID = "gemini-2.5-flash"

# Pergunta ao Gemini uma informação mais recente que seu conhecimento

model = genai.GenerativeModel(MODEL_ID)

resposta = model.generate_content(
    contents= st.text_input('Digite sua pergunta'),
)
# Exibe a resposta na tela
st.write(f"Resposta:\n {resposta.text}")

