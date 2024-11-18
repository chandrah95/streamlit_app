import streamlit as st
import pandas as pd

def campaign_form():
    butarget = ['Retails','AK','AG','AB','FR']
    buyer_target = ['New Buyer','New Buyer with <3 Trx','Existing Buyer(M+2)','Dormant Buyer (>M+2)','New to Component / Channel Buyer','New to Category Buyer','New to Campaign Buyer','New to Brand Buyer','New to SKU Buyer','All','Segmented']
    L0BO = ['Traffic / NB Puller','GMV','Order / # of Buyer','CM','ARPU','None']
    L1BO = ['CVR','AOV','Retention Rate','Order Frequency','Gross Margin','None']
    behavior_objective = ['Quantity per Order Driver','Retention Driver','Frequency Driver','Selling Price per Order Driver','Acquisition']
    
    st.subheader('Campaign Form')

    col1,col2,col3,col4 = st.columns([2,2,2,2])

    with col1:
        campaign_name = st.text_input('Campaign Name') 
    with col2:
        start_date = st.date_input('Start Date')
        start_time = st.time_input('Start Time')
    with col3:
        end_date = st.date_input('End Date')
        end_time = st.time_input('End Time')
    with col4:
        bu_target = st.selectbox('BU Target',butarget)
        st.button('+')


campaign_form()