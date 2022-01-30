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
    sheet_id = st.secrets["fitness_test"]
    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
    st.subheader('Fitness Test Database')
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
        
    ten = df[['YEAR','SPORT','NAME','GENDER','AGE','10 M SPRINT']].dropna()
    st.subheader('10 Meter Sprint (s)')
    st.write(ten)
        
    twenty = df[['YEAR','SPORT','NAME','GENDER','AGE','20 M SPRINT']].dropna()
    st.subheader('20 Meter Sprint (s)')
    st.write(twenty)
        
    forty = df[['YEAR','SPORT','NAME','GENDER','AGE','40 M SPRINT']].dropna()
    st.subheader('40 Meter Sprint (s)')
    st.write(forty)
        
    total = df[['YEAR','SPORT','NAME','GENDER','AGE','TOTAL']].dropna()
    st.subheader('Total Handgrip Strength (kg)')
    st.write(total)
        
    yy = df[['YEAR','SPORT','NAME','GENDER','AGE','YOYO TEST']].dropna()
    st.subheader('Beep Test')
    st.write(yy)
        
    st.header('Filter Fitness Test Data')
    menu = ["YEAR","CATEGORY","SPORT","GENDER"]
    choice = st.selectbox("Chose the filter",menu)
    value = st.selectbox('Chose The '+choice, df[choice].drop_duplicates()) 
    st.subheader('Filter by ('+choice+')')
    a = df.loc[(df[choice]==value)]
    st.write(a)

        
    col1, col2, col3, col4 = st.columns(4) 
    menu_1 = ["YEAR","PHASE","CATEGORY","SPORT","GENDER"]
    choice1 = col1.selectbox("Filter(1)",menu_1)
    choice2 = col2.selectbox("Filter(2)",menu_1)
    choice3 = col3.selectbox("Filter(3)",menu_1)
    choice4 = col4.selectbox("Filter(4)",menu_1)
    col11, col22, col33, col44 = st.columns(4) 
    value1 = col11.selectbox('Chose The '+choice1, df[choice1].drop_duplicates()) 
    value2= col22.selectbox('Chose The '+choice2, df[choice2].drop_duplicates()) 
    value3 = col33.selectbox('Chose The '+choice3, df[choice3].drop_duplicates())  
    value4 = col44.selectbox('Chose The '+choice4, df[choice4].drop_duplicates())  
    if st.checkbox("Filter"):
       a = df.loc[(df[choice1]==value1)&(df[choice2]==value2)&(df[choice3]==value3)&(df[choice4]==value4)]
       file = a[['NAME','BMI','BODY FAT','CMJ','SBJ','TOTAL','SIT & REACH','ILLINOIS/L','ILLINOIS/R','10 M SPRINT','20 M SPRINT','YOYO TEST']]
       st.write(a)
        


