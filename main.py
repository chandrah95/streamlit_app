import streamlit as st
import pandas as pd




def main():
    st.title('Astro Campaign Manager')
    menu = ['Project','Campaign','Activity']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Project':
        st.subheader('Project Form')
        with st.form(key = 'project'):
            project_name = st.text_input('Project Name')
            start_date = st.date_input('Start Date')
            start_time = st.time_input('Start Time')
            end_date = st.date_input('End Date')
            end_time = st.time_input('End Time')

            col1,col2,col3,col4,col5,col6 = st.columns(6)
            with col1:
                submit_button = st.form_submit_button(label = 'Submit')
            with col2:
                cancel_button = st.form_submit_button(label = 'Cancel')
            
            if cancel_button:
                st.session_state['project_name'] = ''
            if submit_button:
                st.write(f'Project Name : {project_name}\n')
                st.write(f'Start Date : {start_date} {start_time}\n')
                st.write(f'End Date : {end_date} {end_time}')


    elif choice == 'Campaign':
        st.subheader('Campaign')
        with st.form(key ='campaign'):
            types = ['KOL','Social Media','Digital Marketing','In App Promo','In App Asset']
            campaign_name = st.txt_input('Campaign_name')
            campaign_type = st.selectbox('Select Campaign Type',types)
            start_date = st.date_imput('Start Date')
            start_time = st.time_input('End Date')
            end_date = st.date_input('End Date')
            end_time = st.time_input('End Time')
            col1,col2,col3,col4,col5,col6 = st.columns(6)
            with col1:
                submit_button = st.form_submit_button(label = 'Submit')
            with col2:
                cancel_button = st.form_submit_button(label = 'Cancel')
    else:
        st.subheader('Activity')

if __name__ == '__main__':
    main()
