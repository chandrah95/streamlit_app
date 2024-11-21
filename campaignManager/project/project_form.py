import streamlit as st
import pandas as pd
from datetime import date,timedelta,datetime,time

def project_form():
    st.subheader('Project Form')

    pf1,pf2,pf3 = st.columns([2,2,2])

    with pf1:
        st.text_input('Project Name')
    
    with pf2:
        maxval = date.today() + timedelta(days = 365)
        try:
            startDateProject,endDateProject = st.date_input('Start Date - End Date',[date.today(),maxval],min_value = date.today())
        except:
            st.error('Tolong isi tanggal Project')
    with pf3:
        start_time = time(9,00)
        end_time = time(9,00)
        start_time_input, end_time_input = st.columns([2,2])
        with start_time_input:
            start_time_select = st.time_input('Start Time',start_time)
        with end_time_input:
            end_time_select = st.time_input('End Time',end_time)


project_form()