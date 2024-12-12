import streamlit as st

def initialize_session_state():

    # Initialize session state in project form
    if 'project_name' not in st.session_state:
        st.session_state['project_name'] = []

    # Initialize session state in campaign form
    if 'campaign_name' not in st.session_state:
        st.session_state['campaign_name'] = []
    if 'bu_target' not in st.session_state:
        st.session_state['bu_target'] = []
    if 'iap_budget' not in st.session_state:
        st.session_state['iap_budget'] = []
    if 'md_budget' not in st.session_state:
        st.session_state['iap_budget'] = []
    if 'ar_budget' not in st.session_state:
        st.session_state['iap_budget'] = []
    if 'buyer_targets' not in st.session_state:
        st.session_state['buyer_targets'] = []
    if 'buyer_target_value' not in st.session_state:
        st.session_state['buyer_target_value'] = [] 

    # Initailize session state in activity KOL form
    if 'kol_act_name' not in st.session_state:
        st.session_state['kol_act_name'] = []
    if 'kol_budget_type' not in st.session_state:
        st.session_state['kol_budget_type'] = []
    if 'kol_budget_value' not in st.session_state:
        st.session_state['kol_budget_value'] = []
    if 'kol_kol_name' not in st.session_state:
        st.session_state['kol_kol_name'] = []
    if 'kol_kol_type' not in st.session_state:
        st.session_state['kol_kol_type'] = []
    if 'kol_channel' not in st.session_state:
        st.session_state['kol_channel'] = []
    if 'kol_follower' not in st.session_state:
        st.session_state['kol_follower'] = []
    if 'kol_utm_link' not in st.session_state:
        st.session_state['kol_utm_link'] = []
    if 'kol_voucher' not in st.session_state:
        st.session_state['kol_voucher'] = []
    if 'kol_buyer_target' not in st.session_state:
        st.session_state['kol_buyer_target'] = []
    if 'kol_L0BO' not in st.session_state:
        st.session_state['kol_L0BO'] = []
    if 'kol_L1BO' not in st.session_state:
        st.session_state['kol_L1BO'] = []
    if 'kol_buyer_target_value' not in st.session_state:
        st.session_state['kol_buyer_target_value'] = []
    if 'kol_L0BO_value' not in st.session_state:
        st.session_state['kol_L0BO_value'] = []
    if 'kol_L1BO_value' not in st.session_state:
        st.session_state['kol_L1BO_value'] = []
    if 'kol_behavior_objective' not in st.session_state:
        st.session_state['kol_behavior_objective'] = []
    if 'kol_secondary_goal' not in st.session_state:
        st.session_state['kol_secondary_goal'] = []
    if 'kol_secondary_goal_value' not in st.session_state:
        st.session_state['kol_secondary_goal_value'] = []
    
    # Initialize session state in activity event form
    if 'event_act_name' not in st.session_state:
        st.session_state['event_act_name'] = []
    if 'event_budget_type' not in st.session_state:
        st.session_state['event_budget_type'] = []
    if 'event_budget_value' not in st.session_state:
        st.session_state['event_budget_value'] = []
    if 'event_event_size' not in st.session_state:
        st.session_state['event_event_size'] = []
    if 'event_event_type' not in st.session_state:
        st.session_state['event_event_type'] = []
    if 'event_utm_link' not in st.session_state:
        st.session_state['event_utm_link'] = []
    if 'event_voucher' not in st.session_state:
        st.session_state['event_voucher'] = []
    if 'event_buyer_target' not in st.session_state:
        st.session_state['event_buyer_target'] = []
    if 'event_L0BO' not in st.session_state:
        st.session_state['event_L0BO'] = []
    if 'event_L1BO' not in st.session_state:
        st.session_state['event_L1BO'] = []
    if 'event_L0BO_value' not in st.session_state:
        st.session_state['event_L0BO_value'] = []
    if 'event_L1BO_value' not in st.session_state:
        st.session_state['event_L1BO_value'] = []
    if 'event_behavior_objective' not in st.session_state:
        st.session_state['event_behavior_objective'] = []
    if 'event_secondary_goal' not in st.session_state:
        st.session_state['event_secondary_goal'] = []
    if 'event_secondary_goal_value' not in st.session_state:
        st.session_state['event_secondary_goal_value'] = []
    
    # Initialize session state in activity digital marketing form
    if 'digimar_act_name' not in st.session_state:
        st.session_state['digimar_act_name'] = []
    if 'digimar_budget_type' not in st.session_state:
        st.session_state['digimar_budget_type'] = []
    if 'digimar_budget_value' not in st.session_state:
        st.session_state['digimar_budget_value'] = []
    if 'digimar_platform' not in st.session_state:
        st.session_state['digimar_platform'] = []
    if 'digimar_ads_format' not in st.session_state:
        st.session_state['digimar_ads_format'] = []
    if 'digimar_ads_objective' not in st.session_state:
        st.session_state['digimar_ads_objective'] = []
    if 'digimar_campaign_name' not in st.session_state:
        st.session_state['digimar_campaign_name'] = []
    if 'digimar_ad_name' not in st.session_state:
        st.session_state['digimar_ad_name'] = []
    if 'digimar_target_audience' not in st.session_state:
        st.session_state['digimar_target_audience'] = []
    if 'digimar_locations' not in st.session_state:
        st.session_state['digimar_locations'] = []
    if 'digimar_main_comms' not in st.session_state:
        st.session_state['digimar_main_comms'] = []
    if 'digimar_brief' not in st.session_state:
        st.session_state['digimar_brief'] = []
    if 'digimar_copy' not in st.session_state:
        st.session_state['digimar_copy'] = []
    if 'digimar_utm_link' not in st.session_state:
        st.session_state['digimar_utm_link'] = []
    if 'digimar_kv_reference' not in st.session_state:
        st.session_state['digimar_kv_reference'] = []
    if 'digimar_product_id' not in st.session_state:
        st.session_state['digimar_product_id'] = []
    if 'digimar_image_url' not in st.session_state:
        st.session_state['digimar_image_url'] = []
    if 'digimar_buyer_target' not in st.session_state:
        st.session_state['digimar_buyer_target'] = []
    if 'digimar_L0BO' not in st.session_state:
        st.session_state['digimar_L0BO'] = []
    if 'digimar_L1BO' not in st.session_state:
        st.session_state['digimar_L1BO'] = []
    if 'digimar_buyer_target_value' not in st.session_state:
        st.session_state['digimar_buyer_target_value'] = []
    if 'digimar_L0BO_value' not in st.session_state:
        st.session_state['digimar_L0BO_value'] = []
    if 'digimar_L1BO_value' not in st.session_state:
        st.session_state['digimar_L1BO_value'] = []
    if 'digimar_behavior_objective' not in st.session_state:
        st.session_state['digimar_behavior_objective'] = []
    if 'digimar_secondary_goal' not in st.session_state:
        st.session_state['digimar_secondary_goal'] = []
    if 'digimar_secondary_goal_value' not in st.session_state:
        st.session_state['digimar_secondary_goal_value'] = []
    
    # Initialize session state in activity socmed form
    if 'socmed_act_name' not in st.session_state:
        st.session_state['socmed_act_name'] = []
    if 'socmed_budget_type' not in st.session_state:
        st.session_state['socmed_budget_type'] = []
    if 'socmed_budget_value' not in st.session_state:
        st.session_state['socmed_budget_value'] = []
    if 'socmed_platform' not in st.session_state:
        st.session_state['socmed_platform'] = []
    if 'socmed_asset_placement' not in st.session_state:
        st.session_state['socmed_asset_placement'] = []
    if 'socmed_asset_format' not in st.session_state:
        st.session_state['socmed_asset_format'] = []
    if 'socmed_content_obj' not in st.session_state:
        st.session_state['socmed_content_obj'] = []
    if 'socmed_type_of_campaign' not in st.session_state:
        st.session_state['socmed_type_of_campaign'] = []
    if 'socmed_headline_cover' not in st.session_state:
        st.session_state['socmed_headline_cover'] = []
    if 'socmed_cover' not in st.session_state:
        st.session_state['socmed_cover'] = []
    if 'socmed_vd_cover' not in st.session_state:
        st.session_state['socmed_vd_cover'] = []
    if 'socmed_caption_feed_reels' not in st.session_state:
        st.session_state['socmed_caption_feed_reels'] = []
    if 'socmed_composite_scene' not in st.session_state:
        st.session_state['socmed_composite_scene'] = []
    if 'socmed_utm_link' not in st.session_state:
        st.session_state['socmed_utm_link'] = []
    if 'socmed_kv_reference' not in st.session_state:
        st.session_state['socmed_kv_reference'] = []
    if 'socmed_product_id' not in st.session_state:
        st.session_state['socmed_product_id'] = []
    if 'socmed_image_url' not in st.session_state:
        st.session_state['socmed_image_url'] = []
    if 'socmed_buyer_target' not in st.session_state:
        st.session_state['socmed_buyer_target'] = []
    if 'socmed_L0BO' not in st.session_state:
        st.session_state['socmed_L0BO'] = []
    if 'socmed_L1BO' not in st.session_state:
        st.session_state['socmed_L1BO'] = []
    if 'socmed_buyer_target_value' not in st.session_state:
        st.session_state['socmed_buyer_target_value'] = []
    if 'socmed_L0BO_value' not in st.session_state:
        st.session_state['socmed_L0BO_value'] = []
    if 'socmed_L1BO_value' not in st.session_state:
        st.session_state['socmed_L1BO_value'] = []
    if 'socmed_behavior_objective' not in st.session_state:
        st.session_state['socmed_behavior_objective'] = []
    if 'socmed_secondary_goal' not in st.session_state:
        st.session_state['socmed_secondary_goal'] = []
    if 'socmed_secondary_goal_value' not in st.session_state:
        st.session_state['socmed_secondary_goal_value'] = []
    
    # Initialize session state in activity In App Asset form
    