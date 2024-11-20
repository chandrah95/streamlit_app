import streamlit as st
import pandas as pd
from datetime import time, timedelta,datetime
import random
import string

def main_page(user_id,name,division,activity,create,approving):
    
    initialize_session_state()

    if session_state['main_page'] == 'Create New Project':
        project_item(user_id,name,division)
    
    if session_state[]