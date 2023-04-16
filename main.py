import streamlit as st
st.title("Finding the Biggest of the Three Numbers")
n1 = st.number_input("Input the first number")
n2 = st.number_input("Input the second number")
n3 = st.number_input("Input the third number")
st.subheader("The first number is " + str(n1))
st.subheader("The second number is " + str(n2))
st.subheader("The third number is " + str(n3))

if st.button("Find Highest"):
    if n1 >= n2 and n1 >= n3:
        st.header(str(n1) + " is the biggest number")

    elif n2 >= n3 and n2 >= n1:
        st.header(str(n2) + " is the biggest number")

    else:
        st.header(str(n3) + " is the biggest number")

