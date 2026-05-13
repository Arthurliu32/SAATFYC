import streamlit as st
from openai import OpenAI


client = OpenAI(
    api_key= st.secrets['OPENAIKEY']
)

