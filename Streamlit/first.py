import streamlit as st
st.title('Calculator')
st.write("number 1")
x = st.number_input("enter first number", step=1)
# step = 1 is type (int)
y = st.number_input("enter second number", step=1)
n = x + y
if st.button(label="Addition"):
    st.write(n)

