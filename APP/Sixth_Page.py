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
    st.text_input("Pasword")
    psw = st.text_input("Password", type='password')
    if psw == st.secrets["password_1"]:
        sheet_id = st.secret[fitness_test]
        df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
        st.write(df)
