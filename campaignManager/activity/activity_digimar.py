import streamlit as st
import pandas as pd
from datetime import time,timedelta,date,datetime


def activity_digimar():
    
    platform_option = ['Meta','Tiktok','Google','X','Others']
    ads_format_option = ['Meta - Banner','Meta - Video','Meta - Carousel','Meta - Collection','Google - Search','Google - Display','Google - Shopping','Google - Video','Google - App','Google - Discovery','Google - PMAX','Google - Smart','TikTok - Image','TikTok - Video','TikTok - Motion','X']
    ads_objective = ['Sales','Traffic','Website Traffic','App Promotion - App Installs','App Promotion - App Engagement','Awareness & Consideration','Local Shop Visits and Promotions','Manual','Reach - Auction Reach','Reach - Reach & Frequency','Traffic','Video Views','Community Interaction','App Promotion - App Installs','App Promotion - App Retargeting','Lead Generation','Website Conversions','Product Sales - Catalog','Product Sales - TikTok Shop','Awareness - Maximize Ad Reach','Awareness - Maximize Impressions','Awareness - Maximize Ad Recall Improvement','Awareness - Maximize Thruplay Impressions','Awareness - Continuous Video Playback to 2 Seconds','Traffic - Maximize Link Clicks','Traffic - Maximize Number of Daily Unique Reach','Traffic - Maximize Conversations','Traffic - Maximize Impressions','Engagement - Maximize Conversations','Engagement - Maximize Link Clicks','Leads','App Promotion - Maximize App Events','App Promotion - Maximize App Installs','App Promotion - Maximize Conversion Value','App Promotion - Maximize Link Clicks','App Promotion - Maximize Conversions','Sales - Maximize Conversions','Sales - Conversion Value','Sales - Maximize Link Clicks','Sales - Maximize Impressions']
    kv_type_option = ['Image','Video','Motion']
    kv_size = ['1:1','16:9','9:16']
    is_req_new = ['Yes','No']
    digimar_buyer_target = ['New Buyer','New Buyer with <3 trx','Existing Buyer (M+2)','Dormant Buyer (>M+2)','New to Component / Channel Buyer','New to Category Buyer','New to Campaign Buyer','New to Brand Buyer','New to SKU Buyer','All','Segmented']
    digimar_L0BO = ['Traffic / NB Puller','GMV','Order / # of Buyer','CM','ARPU','None']
    digimar_L1BO = ['CVR','AOV','Retention Rate','Order Frequency','Gross Margin','None']
    digimar_behavior_objective = ['Quantity per Order Driver','Retention Driver','Frequency Driver','Selling Price per Order Driver','Acquisition']
    digimar_secondary_goal = ['GMV','GMV New Buyer','GMV Existing Buyer','Total Traffic (Session)','New Buyer Traffic (Session)','Existing Buyer Traffic (Session)','# Buyer','# New Buyer','# of New Buyer with 1st trx','# of New Buyer with 2nd trx','# of New Buyer with >3 trx','# Existing Buyer','# Reactivated Dormant Buyer','Order','Order New Buyer','Order Existing Buyer','Install','CPM (Cost per Millie)','CTR (Click through rate)','CPC (Cost per conversions)','ROAS']
    budget_type = ['In App Promotion','Marketing & Digital','Ads Revenue']

    st.set_page_config(
    page_title = 'Activity Form - KOL',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='auto'
    )

    st.title('Activity Form - Digital Marketing')

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

    st.write(':grey[**Platform Details**]')

    pl1,pl2,pl3 = st.columns([2,2,2])
    with pl1:
        digimar_platform = st.selectbox('Platform',options = platform_option, index = None, placeholder = 'Select option')
    with pl2:
        digimar_ads_format = st.selectbox('Ads Format', options = ads_format_option, index = None , placeholder = 'Select option')
    with pl3:
        digimar_ads_objective = st.selectbox('Ads Objective',options = ads_objective,index = None, placeholder = 'Select option')
    
    st.markdown('---')

    st.write(':grey[**Ads Details**]')

    ads1,ads2 = st.columns([2,4])
    with ads1:
        dm_campaign_name = st.text_input('Campaign Name')
        dm_adgroup_name = st.text_input('Adgroup Name')
        dm_ad_name = st.text_input('Ad/Asset Name')
        dm_target_audience = st.text_input('Target Audience')
        dm_locations = st.text_input('Locations')
    with ads2:
        dm_main_comm = st.text_input('Main Comms')
        dm_brief = st.text_input('Brief')
        dm_copy = st.text_input('Copy')
        dm_utm = st.text_input('UTM Link')
        dm_kv_reference = st.text_input('KV Reference')
    
    st.markdown('---')
    st.write(':grey[**Product Details**]')
    
    pd1,pd2 = st.columns([2,4])
    with pd1:
        dm_product_id = st.text_input('Product ID')
    with pd2:
        dm_product_image = st.text_input('Image URL')

        st.markdown('---')
    st.write(':grey[**Primary Goal**]')

    pg1,pg2 = st.columns([2,2])
    with pg1:
        with st.container():
            cols = st.columns([5,3,1])
            with cols[0]:
                buyer_target_fill= st.selectbox('Buyer Target',digimar_buyer_target)
                L0BO_fill = st.selectbox('L0 Business Objective',digimar_L0BO)
                L1BO_fill = st.selectbox('L1 Business Objective',digimar_L1BO)
            with cols[1]:
                buyer_target_value_fill = st.number_input('Buyer Target Value',min_value = 0, step = 1)
                L0BO_value_fill = st.number_input('L0 Business Objective Value',min_value = 0, step = 1)
                L1BO_value_fill = st.number_input('L1 Business Objective Value',min_value = 0, step = 1   )
            with cols[2]:
                st.caption('')
                st.caption('')

    st.markdown('---')
    st.subheader(':grey[**Secondary Goal**]')

    sg1,sg2 = st.columns([2,2])
    with sg1:
        with st.container():
            cols = st.columns([5,3,1])
            with cols[0]:
                secondary_goal_fill = st.selectbox('Secondary Goal',digimar_secondary_goal)
            with cols[1]:
                seconday_goal_value_fill = st.number_input('Secondary Goal Value',min_value = 0, step = 1)

    
    sb1,sb2,sb3 = st.columns([1,1,1])
    with sb1:
        cols = st.columns([1,1,1,1])
        with cols[0]:
            submit_button = st.button('Submit')
        with cols[1]:
            cancel_button = st.button('Cancel')
activity_digimar()