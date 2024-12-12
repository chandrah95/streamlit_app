import streamlit as st
import pandas as pd
from datetime import time,timedelta,date,datetime

def activity_socmed():
    budget_type =   ['In App Promotion','Marketing & Digital','Ads Revenue']
    platform = ['IG','TikTok']
    asset_placement = ['Story','Feed','Reels']
    asset_format = ['Static Image','Video Motion','Video Real']
    content_objective = ['Awareness','Engagement','Conversions']
    type_of_campaign = ['Promotion - Voucher Code','Promotion - Giveaway','Promotion - Campaign','Entertainment - General','Entertainment - Viral Trend','Entertainment - UGC','Inspiration','Recipe','Repost - Random','Repost - KOL (unpaid)','Repost - KOL (Paid)']
    buyer_target = ['New Buyer','New Buyer with <3 trx','Existing Buyer (M+2)','Dormant Buyer (>M+2)','New to Component / Channel Buyer','New to Category Buyer','New to Campaign Buyer','New to Brand Buyer','New to SKU Buyer','All','Segmented']
    L0BO = ['Traffic / NB Puller','GMV','Order / # of Buyer','CM','ARPU','None']
    L1BO = ['CVR','AOV','Retention Rate','Order Frequency','Gross Margin','None']
    behavior_objective = ['Quantity per Order Driver','Retention Driver','Frequency Driver','Selling Price per Order Driver','Acquisition']
    secondary_goal = [' Conversions',' Reach',' Impressions',' Total Engagements',' Comments',' Mentions',' Share',' Saves',' Replies'] 

    st.set_page_config(
        page_title = 'Activity Form - Social Media',
        page_icon = '📋',
        layout = 'wide',
        initial_sidebar_state = 'collapsed'
    )

    st.title('Activity Form - Social Media')
    
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

    pd1,pd2 = st.columns([2,2])
    with pd1:
        sm_platform = st.selectbox('Platform',options = platform, index = None, placeholder = 'Select Option')
        sm_asset_placement = st.selectbox('Asset Placement', options = asset_placement, index = None , placeholder = 'Select Option')
        sm_asset_format = st.selectbox('Asset Format',options = asset_format, index = None, placeholder = 'Select Option')
    with pd2:
        sm_content_objective = st.selectbox('Content Objective',options = content_objective, index = None , placeholder = 'Select Option')
        sm_campaign_type = st.selectbox('Type of Campaign', options = type_of_campaign, index = None, placeholder = 'Select Option')
    
    st.markdown('---')
    st.write(':grey[**Ads Details**]')

    ads1,ads2 = st.columns([2,4])
    with ads1:
        sm_headline_cover = st.text_input('Headline Cover')
        sm_cover = st.text_input('Cover')
        sm_visual_direction_cover = st.text_input('Visul Direction Cover')
        sm_talent = st.text_input('Talent')
        sm_caption_feed_or_reels = st.text_input('Caption Feed/Reels')
    with ads2:
        sm_composite_scene = st.text_input('Composite Scene')
    
    sm_utm = st.text_input('UTM Link')
    sm_kv_reference = st.text_input('KV Reference')

    st.markdown('---')
    st.write(':grey[**Product Details**]')

    pd1,pd2 = st.columns([2,4])
    with pd1:
        sm_product_id = st.text_input('Product ID')
    with pd2:
        sm_product_image = st.text_input('Image URL')
    
    st.markdown('---')
    st.write(':grey[**Primary Goal**]')

    pg1,pg2 = st.columns([3,2])
    with pg1:
        with st.container():
            cols = st.columns([2,1])
            with cols[0]:
                buyer_target_fill= st.selectbox('Buyer Target',buyer_target)
                L0BO_fill = st.selectbox('L0 Business Objective',L0BO)
                L1BO_fill = st.selectbox('L1 Business Objective',L1BO)
            with cols[1]:
                buyer_target_value_fill = st.number_input('Buyer Target Value',min_value = 0, step = 1)
                L0BO_value_fill = st.number_input('L0 Business Objective Value',min_value = 0, step = 1)
                L1BO_value_fill = st.number_input('L1 Business Objective Value',min_value = 0, step = 1   )
    with pg2:
            socmed_behavior_obj = st.selectbox('Behavior Objective',options = behavior_objective, index = None, placeholder = 'Select Option')
            st.caption('')
            st.caption('')

    st.markdown('---')
    st.subheader(':grey[**Secondary Goal**]')

    sg1,sg2 = st.columns([2,2])
    with sg1:
        with st.container():
            cols = st.columns([5,3,1])
            with cols[0]:
                secondary_goal_fill = st.selectbox('Secondary Goal',secondary_goal)
            with cols[1]:
                seconday_goal_value_fill = st.number_input('Secondary Goal Value',min_value = 0, step = 1)

    
    sb1,sb2,sb3 = st.columns([1,1,1])
    with sb1:
        cols = st.columns([1,1,1,1])
        with cols[0]:
            submit_button = st.button('Submit')
        with cols[1]:
            cancel_button = st.button('Cancel')

activity_socmed()