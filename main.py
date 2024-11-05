import streamlit as st
import pandas as pd

def login_menu():
    st.header('Astro UTM')
    with st.form(key ='login', clear_on_submit = True, border = True):
        username = st.text_input('Username')
        password = st.text_input('Password')
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            submit = st.form_submit_button('Submit')
        with col2:
            cancel = st.form_submit_button('Cancel')
        
        if submit:
            st.write('Welcome!\n')
            st.write(username)  

login_menu()