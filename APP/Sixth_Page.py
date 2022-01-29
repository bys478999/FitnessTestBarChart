import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.graph_objects as go
import openpyxl

def app():
    st.title('Fitness Test Result')
    password = st.text_input("Password")
    if password == st.secrets["password_1"]:
        sheet_id = st.secrets["fitness_test"]
        df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
        st.write(df)
        bodyfat = df[['YEAR','SPORT','NAME','GENDER','AGE','BODY FAT']]
        bf = bodyfat.dropna()
        st.subheader('Body Fat (%)')
        st.write(bf)
        
        maximumpushup = df[['YEAR','SPORT','NAME','GENDER','AGE','MAXIMUM PUSH UP']]
        mpu = maximumpushup.dropna()
        st.subheader('Maximum Push Up (Repetition)')
        st.write(mpu)
        
        situp = df[['YEAR','SPORT','NAME','GENDER','AGE','1 MIN SIT UP']]
        su = situp.dropna()
        st.subheader('1 Minute Sit Up (Repetition)')
        st.write(su)
    
    
    else:
        st.warning("Incorrect Password")
