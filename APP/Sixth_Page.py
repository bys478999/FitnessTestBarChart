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
    file = st.file_uploader("Chose a file")
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(round(df, 2))
        st.sidebar.header('Fitness Test')
        y_value = st.sidebar.selectbox('Test', df.columns)
