import streamlit as st
st.title("WEEEEEHAAAAAAAAAAAAAAAAA!") 


num1=st.number_input("enter num1",step=2)
num2=st.number_input("enter num2",step=1)
sum = num1+num2
if st.button("ADD THIS"):
    st.write("sum is: ",sum)

num3=st.number_input("enter num3",step=1)
num4=st.number_input("enter num4",step=1)
dif = num3-num4
if st.button("minus THIS"):
    st.write("sum is: ",dif)

num5=st.number_input("enter num5",step=1)
num6=st.number_input("enter num6",step=1)
mul = num5*num6
if st.button("MULTIPLY THIS"):
    st.write("sum is: ",mul)

num7=st.number_input("enter num7",step=1)
num8=st.number_input("enter num8",step=1)
div = num7/num8
if st.button("divi THIS"):
    st.write("sum is: ",div)