import streamlit as st
import pandas as pd
import openpyxl




def app():
    st.title('Merge Data')
    file_1 = st.file_uploader("Chose a file for pre")
    file_2= st.file_uploader("Chose a file for post")
    if file_2 is not None:
        df = pd.read_excel(file_1)
        df1 = pd.read_excel(file_2)
        a = df.merge(df1, left_on='NAME', right_on='NAME',suffixes=('_1', '_2'), how='outer')
        st.write(a)
        st.download_button(label='Download the dataframe',data=a.to_csv(),mime='text/csv', file_name='Pre & Post Test Comparison.csv')
        
