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
    sheet_id = st.secrets[username]
    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/1TC9AEUCek1gqyrkHFV92iCDHPphV3Ke3LkctMBJ8siE/export?format=xlsx")
