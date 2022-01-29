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
        bf = df[['YEAR','SPORT','NAME','GENDER','AGE','BODY FAT']].dropna()
        st.subheader('Body Fat (%)')
        st.write(bf)
        
        mpu = df[['YEAR','SPORT','NAME','GENDER','AGE','MAXIMUM PUSH UP']].dropna()
        st.subheader('Maximum Push Up (Repetition)')
        st.write(mpu)
        
        su = df[['YEAR','SPORT','NAME','GENDER','AGE','1 MIN SIT UP']].dropna()
        st.subheader('1 Minute Sit Up (Repetition)')
        st.write(su)
        
        sbj = df[['YEAR','SPORT','NAME','GENDER','AGE','SBJ']].dropna()
        st.subheader('Standing Broad Jump (cm)')
        st.write(sbj)
        
        cmj = df[['YEAR','SPORT','NAME','GENDER','AGE','CMJ']].dropna()
        st.subheader('Counter Movement Jump (cm)')
        st.write(cmj)
        
        agility = df[['YEAR','SPORT','NAME','GENDER','AGE','ILLINOIS']].dropna()
        st.subheader('Illinois Test (s)')
        st.write(agility)
        
        sr = df[['YEAR','SPORT','NAME','GENDER','AGE','SIT & REACH']].dropna()
        st.subheader('Sit & Reach (cm)')
        st.write(sr)
        
        10m = df[['YEAR','SPORT','NAME','GENDER','AGE','10 M SPRINT']].dropna()
        st.subheader('10 Meter Sprint (s)')
        st.write(10m)
        
        20m = df[['YEAR','SPORT','NAME','GENDER','AGE','20 M SPRINT']].dropna()
        st.subheader('20 Meter Sprint (s)')
        st.write(20m)
        
        40m = df[['YEAR','SPORT','NAME','GENDER','AGE','40 M SPRINT']].dropna()
        st.subheader('40 Meter Sprint (s)')
        st.write(40m)
        
        total = df[['YEAR','SPORT','NAME','GENDER','AGE','TOTAL']].dropna()
        st.subheader('Total Handgrip Strength (kg)')
        st.write(total)
        
        yy = df[['YEAR','SPORT','NAME','GENDER','AGE','YOYO']].dropna()
        st.subheader('Beep Test')
        st.write(yy)
    
    else:
        st.warning("Incorrect Password")
