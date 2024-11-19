import pandas as pd
import streamlit as st
import random
import string




def format_rupiah(value):
    return "Rp {:,.0f}".format(value)

def generate_random_alphanumeric(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def clear_primary_goals():
    st.session_state['buyer_targets'] = []
    st.session_state['buyer_target_value'] = []
    st.session_state['l0_business_obj'] = []
    st.session_state['l0_business_obj_value']
    st.session_state['l1_business_obj'] = []
    st.session_state['l1_business_obj_value']
    st.session_state['behavior_obj']
