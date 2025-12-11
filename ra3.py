#python -m streamlit run ra.py


import streamlit as st
st.title("how many times more?")
username=st.text_input("enter username ")
password=st.text_input("enter password ")
if st.button("login"):
    if username=="admini":
       if password=="1235":
          st.success("DOUBLE BACON CHEEEESE!!")
       else:
          st.error("JALAPENOES")
    else:
       st.error("HABANEORO")