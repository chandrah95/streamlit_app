import streamlit as st
import pandas as pd
from datetime import time,timedelta,date,datetime

def activity_iaa():
    ads_revenue_type = ['JBP','Cash (One Off)','Barter','None']
    kv_type = ['HPB Dedicated','HPB Mixed','2x2','KV Catalog Tile Small','KV Catalog Tile Big','Pop - Up']
    slot_request = [1,2,3,4,5]
    discount_type = ['Precentage ','Harga Coret','USP','Buy X Get Y','Price Point']
    secondary_promo_copy = ['Flash Sale','Free Ongkir','Voucher','Free Gift','None']
    objective = ['Traffic','Conversion']
    buyer_target = ['New Buyer','New Buyer with <3 trx','Existing Buyer (M+2)','Dormant Buyer (>M+2)','New to Component / Channel Buyer','New to Category Buyer','New to Campaign Buyer','New to Brand Buyer','New to SKU Buyer','All','Segmented']
    L0BO = ['Traffic / NB Puller','GMV','Order / # of Buyer','CM','ARPU','None']
    L1BO = ['CVR','AOV','Retention Rate','Order Frequency','Gross Margin','None']
    behavior_objective = ['Quantity per Order Driver','Retention Driver','Frequency Driver','Selling Price per Order Driver','Acquisition']
    secondary_goal = ['CTR','CVR','GV','GV New to Brand Buyer','CVR New to Brand Buyer']
    budget_type = ['In App Promotion','Marketing & Digital','Ads Revenue']
    st.set_page_config(
        page_title = 'Activity Form - In App Asset',
        page_icon = '📋',
        layout = 'wide',
        initial_sidebar_state = 'expanded'
    )

    st.title('Activity Form - In App Asset')

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
    st.write(':grey[**Ads Details**]')

    ads1,ads2,ads3,ads4 = st.columns([2,1,2.5,2.5])
    with ads1:
        iaa_ads_revenue_type = st.selectbox('Ads Revenue Type',options = ads_revenue_type, index = None, placeholder = 'Select Option')
    with ads2:
        iaa_ads_revenue = st.number_input('Ads Revenue Value', min_value = 0, step = 500)
    with ads3:
        iaa_kv_type = st.selectbox('KV Type',options = kv_type, index = None, placeholder = 'Select Option')
    with ads4:    
        iaa_slot_request = st.selectbox('Slot Request',options = slot_request, index = None, placeholder = 'Select Option')

    st.markdown('---')

    st.write(':grey[**Discount Details**]')

    dd1,dd2 = st.columns([2,4])
    with dd1:
        iaa_max_dc = st.number_input('Max Discount', min_value = 0.0,step = 0.1)
        iaa_avg_dc = st.number_input('Avg Discount',min_value = 0.0,step = 0.1)
        iaa_brand_support = st.number_input('Brand Support / Rafaksi',min_value = 0, step = 500)
    with dd2:
        iaa_discount_type = st.selectbox('Type of Discount',options = discount_type, index = None, placeholder = 'Select Option')
    
    st.markdown('---')
    st.write(':grey[**KV Details**]')

    kd1,kd2 = st.columns([2,4])
    with kd1:
        iaa_ribbon = st.text_input('Ribbon')
        iaa_promo_copy = st.text_input('Promo Copy')
        iaa_secondary_promo_copy = st.selectbox('Secondary Promo Copy',options = secondary_promo_copy, index = None, placeholder = 'Select Option')
    with kd2:
        iaa_remarks = st.text_input('Remarks')
        iaa_cta = st.text_input('Call to Action')
        iaa_objective = st.selectbox('Objective',options = objective, index= 0, placeholder = 'Select Option')

    iaa_brand_logo = st.text_input('Brand Logo',placeholder = 'Input Link')
    iaa_kv_reference = st.text_input('KV Reference')
    st.markdown('---')

    st.write(':grey[**Product Details**]')

    pd1,pd2 = st.columns([2,4])
    with pd1:
        iaa_product_id = st.text_input('Product_id')
    with pd2:
        iaa_product_image = st.text_input('Image URL')
    
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
            iaa_behavior_obj = st.selectbox('Behavior Objective',options = behavior_objective, index = None, placeholder = 'Select Option')
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


activity_iaa()