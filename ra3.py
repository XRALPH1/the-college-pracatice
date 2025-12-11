#python -m streamlit run ra.py
#or streamlit run (ourfile name) ra.py
#go to the di9rectory where our file is located and in the path type cmd 
#and type the above two lo any one to go to the streamlit and view your programme


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