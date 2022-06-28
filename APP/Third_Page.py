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
        a_1 = a[["NAME","YEAR_1","YEAR_2","SPORT_1","SPORT_2","AGE_1","AGE_2","HEIGHT_1","HEIGHT_2","WEIGHT_1","WEIGHT_2","BMI_1","BMI_2","BODY FAT_1","BODY FAT_2","MAXIMUM PUSH UP_1","MAXIMUM PUSH UP_2","1 MIN CURL UP_1","1 MIN CURL UP_2","CMJ_1","CMJ_2","SBJ_1","SBJ_2","TOTAL_1","TOTAL_2","10 M SPRINT_1","10 M SPRINT_2","20 M SPRINT_1","20 M SPRINT_2","40 M SPRINT_1","40 M SPRINT_2","ILLINOIS/L_1","ILLINOIS/L_2","ILLINOIS/R_1","ILLINOIS/R_2","SIT & REACH_1","SIT & REACH_2","YOYO TEST_1","YOYO TEST_2","NOTE_1","NOTE_2"]]
        st.write(a_1)
        st.download_button(label='Download the dataframe',data=a_1.to_csv(),mime='text/csv', file_name='Pre & Post Test Comparison.csv')
 
        
