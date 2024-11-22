import streamlit as st

def initialize_session_state():

    if 'buyer_targets' not in st.session_state:
        st.session_state['buyer_targets'] = []
    if 'buyer_target_value' not in st.session_state:
        st.session_state['buyer_target_value'] = []