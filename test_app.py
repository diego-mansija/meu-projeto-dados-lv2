import streamlit as st

st.title("Olá, Linux Mint!")
st.write("Se você está vendo isso, o Streamlit está rodando perfeitamente no seu ambiente virtual.")

if st.button("Clique aqui"):
    st.balloons() # Um pequeno "easter egg" visual do Streamlit