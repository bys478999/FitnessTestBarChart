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
        st.subheader('Body Fat (%)')
        st.write(bodyfat)
    
    
    else:
        st.warning("Incorrect Password")
