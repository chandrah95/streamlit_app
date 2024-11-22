import streamlit as st
import pandas as pd
from datetime import date, timedelta, datetime,time

def activity_kol():
    st.set_page_config(
    page_title = 'Activity Form - KOL',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='auto'
    )

    budget_type = ['In App Promotion','Marketing & Digital','Ads Revenue']

    st.title('Activity Form - KOL')

    ad1,ad2,ad3 = st.columns([2,2,2])
    with ad1:
        act_name = st.text_input('Activity Name')
    with ad2:
        maxval = date.today() + timedelta(days = 30)
        start_time = time(00,00)
        end_time = time(00,00)
        try:
            startDateKol,endDateKol = st.date_input('Start Date - End Date',[date.today(),maxval], min_value = date.today())
        except:
            st.error('Tolong isi tanggal Activity')

        start_time_input,end_time_input = st.columns([2,2])
        with start_time_input:
            start_time_select = st.time_input('Start Time',start_time)
        with end_time_input:
            end_time_select = st.time_input('End Time',end_time)
    with ad3:
        budget_type = st.selectbox('budget_type',options = budget_type)
        activity_budget = st.text_input('Activity Budget')
    activity_description = st.text_area('Description', height = 100)
    
    st.markdown('---')
    
    st.write(':grey[**KOL Details**]')

    kol_details = st.columns([2,4])

    with kol_details[0]:
        cols = st.columns([0.5,2])
        with cols[0]:
            st.write('KOL Name',unsafe_allow_html = True)
        with cols[1]:
            kol_name = st.text_input('KOL Name',label_visibility = 'collapsed')


activity_kol()