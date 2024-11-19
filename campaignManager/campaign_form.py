import streamlit as st
import pandas as pd
from datetime import date, timedelta,datetime,time
from utils.utils import *

def campaign_form():
    butarget = ['Retails','AK','AG','AB','FR']
    buyer_target = ['New Buyer','New Buyer with <3 Trx','Existing Buyer(M+2)','Dormant Buyer (>M+2)','New to Component / Channel Buyer','New to Category Buyer','New to Campaign Buyer','New to Brand Buyer','New to SKU Buyer','All','Segmented']
    L0BO = ['Traffic / NB Puller','GMV','Order / # of Buyer','CM','ARPU','None']
    L1BO = ['CVR','AOV','Retention Rate','Order Frequency','Gross Margin','None']
    behavior_objective = ['Quantity per Order Driver','Retention Driver','Frequency Driver','Selling Price per Order Driver','Acquisition']
    
    st.set_page_config(
    page_title='Campaign Form',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='auto'
    )

    st.subheader('Campaign Form')

    col1,col2,col3,col4 = st.columns([1,1,1,1])

    with col1:
        campaign_name = st.text_input('Campaign Name') 
    with col2:
        maxval = date.today() + timedelta(days = 90)
        try:
            startDateCampaign,endDateCampaign = st.date_input('Start Date - End Date',[date.today(),maxval],min_value = date.today())
        except:
            st.error('Tolong isi tanggal Campaign')
    with col3:
        start_time = time(00,00)
        end_time = time(00,00)
        start_time_input,end_time_input = st.columns([2,2])
        with start_time_input:
            start_time_select = st.time_input('Start Time',start_time)
        with end_time_input:
            end_time_select = st.time_input('End Time',end_time)
    with col4:
        bu_target = st.selectbox('BU Target',butarget)
    st.text_area('Description',height = 100, max_chars = 500)
    
    st.markdown('---')

    st.write(':gray[**Requested Budget**]',unsafe_allow_html= True)

    cols = st.columns([2,2,2])
    with cols[0]:
        st.text_input('In App Promotion')
    with cols[1]:
        st.text_input('Marketing & Digital')
    with cols[2]:
        st.text_input('Ads Revenue')

    st.markdown('---')
    st.write(':gray[**Primary Goal**]',unsafe_allow_html= True)

    pg1,pg2 = st.columns([2,2])
    with pg1:
        with st.container():
            buyer_target_options = buyer_target 
            for i, (buyer_target, values) in enumerate(zip(st.session_state['buyer_targets'], st.session_state['buyer_target_value'])):
                available_options = [opt for opt in buyer_target_options if opt not in st.session_state['buyer_targets'] or opt == buyer_target]
                cols = st.columns([2,1,1])
                with cols[0]:
                    st.session_state['buyer_targets'][i] = st.selectbox(f'Buyer Target{i + 1}', available_options, index = available_options.index(buyer_target), key = f'buyer_target_{i}')
                with cols[1]:
                    st.session_state['buyer_target_value'][i] = st.number_input('Value',min_value = 0, step = 1,value = int(values), key = f'value_{i}')
                with cols[2]:
                    st.caption('')
                    st.caption('')
                    if st.button('❌', key=f'delete_buyer_target_{i}'):
                        del st.session_state['buyer_targets'][i]
                        del st.session_state['buyer_target_value'][i]
                        st.rerun()

    # p2c1, p2c2 = st.columns([2, 2])
    # with p2c1:
    #     st.subheader('Budget')
    #     with st.container():
    #         options = budget_options
    #         for i, (grouping, budget) in enumerate(zip(st.session_state['activity_groupings'], st.session_state['activity_grouping_budgets'])):
    #             available_options = [opt for opt in options if opt not in st.session_state['activity_groupings'] or opt == grouping]
    #             cols = st.columns([2, 1, 1])
    #             with cols[0]:
    #                 st.session_state['activity_groupings'][i] = st.selectbox(f'Activity {i + 1}', available_options, index=available_options.index(grouping), key=f'activity_{i}')
    #             with cols[1]:
    #                 st.session_state['activity_grouping_budgets'][i] = st.number_input(f'Budget for {grouping}', min_value=0, step=1, value=int(budget), key=f'budget_{i}')
    #             with cols[2]:
    #                 st.caption('')
    #                 st.caption('')
    #                 if st.button('❌', key=f'delete_activity_{i}'):
    #                     del st.session_state['activity_groupings'][i]
    #                     del st.session_state['activity_grouping_budgets'][i]
    #                     st.rerun()

campaign_form()