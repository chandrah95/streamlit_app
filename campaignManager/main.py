import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import re


st.set_page_config(
    page_title = 'Astro UTM',
    page_icon = ':loud_sound:',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

d = {
    'usersId' : [],
    'names' : [],
    'usernames' : [],
    'hashed_passwords' : [],
    'divisi' : [],
    'access' : []
}

@st.cache_data(show_spinner= False)

def load_auth():
    users_id = pd.read_csv('login.csv')
    users_id = users_id.drop_duplicates(subset = ['id'])
    usernames = users_id['email'].values.tolist()
    passwords = users_id['password'].astype(str).values.tolist()
    hashed_passwords = stauth.Hasher(passwords).generate()
    names = users_id['name'].values.tolist()
    return users_id,usernames,passwords,hashed_passwords,names


def clear_cache():
    load_auth.clear()

d['usersId'],d['usernames'],d['passwords'],d['hashed_passwords'],d['names'] = load_auth()

credentials = {
    'usernames' : {
        username :{'name' : name, 'password' : hashed_password}
        for username, name, hashed_password in zip(d['usernames'],d['names'],d['hashed_passwords'])
    }
}

authenticator = stauth.Authenticate(
    credentials = credentials,
    cookie_name = 'astromarketing',
    cookie_key = 'astro_keys21',
    cookie_expiry_days = 360 
)

name,authentication_status,username = authenticator.login('main')

if authentication_status:
    user_data = d['usersId'][d['usersId']['email'] == username]
    user_id = user_data['id'].values[0]
    name = user_data['name'].values[0]
    division = user_data['divisi'].values[0]
    activity = user_data['activity'].astype(str).item()
    create = user_data['create'].astype(str).item()
    approving = user_data['approval'].astype(str).item()

    with st.sidebar:
        authenticator.logout('Logout','main')
        st.write(f'Welcome *{name}*')

        approving = str(approving)
        main_page(user_id,name,division,activity,create,approving)

elif authentication_status == False:
    st.error('Username/Password is incorrect')
elif authentication_status == None:
    st.warning('Please enter Username & Password')

    