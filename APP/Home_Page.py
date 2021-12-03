import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.graph_objects as go
import openpyxl

def app():
    st.title('Bar Chart Maker')
    file = st.file_uploader("Chose a file")
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(round(df, 2))
        st.sidebar.header('Fitness Test')
        y_value = st.sidebar.selectbox('Test', df.columns)

        def load_data(y):
            if y == 'NAME':
                st.dataframe(df['NAME'])

            elif y == 'BMI':
                x = df['NAME']
                y = round(df['BMI'].astype(float), 2)
                sorted_y = df.sort_values(by=['BMI'])
                cc = ['colors'] * len(y)
                a_BMI = 18.5
                b_BMI = 18.5
                b1_BMI = 24.9
                c_BMI = 25
                c1_BMI = 29.9
                d_BMI = 29.9
                for n, val in enumerate(y):
                    if val < a_BMI:
                        cc[n] = 'green'
                    elif val >= b_BMI and val <= b1_BMI:
                        cc[n] = 'lime'
                    elif val >= c_BMI and val <= c1_BMI:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 40., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 100., 35.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, data=sorted_y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("BMI")
                plt.ylabel("BMI Score")
                plt.ylim(xx, yy)
                BMI1 = mpatches.Patch(color='green', label='Underweight (' + '<' + str(a_BMI) + ')')
                BMI2 = mpatches.Patch(color='lime', label='Normal (' + str(b_BMI) + '-' + str(b1_BMI) + ')')
                BMI3 = mpatches.Patch(color='yellow', label='Overweight (' + str(c_BMI) + '-' + str(c1_BMI) + ')')
                BMI4 = mpatches.Patch(color='darkgoldenrod', label='Obesity (' + '>' + str(d_BMI) + ')')
                plt.legend(handles=[BMI1, BMI2, BMI3, BMI4], loc="upper right", bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'BODY FAT':
                x = df['NAME']
                y = round(df['BODY FAT'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_BF = 20
                b_BF = 19
                for n, val in enumerate(y):
                    if val < a_BF:
                        cc[n] = 'green'
                    else:
                        cc[n] = 'yellow'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 40., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 40., 30.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Body Fat")
                plt.ylabel("Body Fat (%)")
                plt.ylim(xx, yy)
                BF1 = mpatches.Patch(color='green', label='Normal (<' + str(a_BF) + ')')
                BF2 = mpatches.Patch(color='yellow', label='Overweight (>' + str(b_BF) + ')')
                plt.legend(handles=[BF1, BF2], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'MAXIMUM PUSH UP':
                x = df['NAME']
                y = round(df['MAXIMUM PUSH UP'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_MPU = 1
                b_MPU = 2
                b1_MPU = 3
                c_MPU = 4
                c1_MPU = 5
                d_MPU = 6
                for n, val in enumerate(y):
                    if val < a_MPU:
                        cc[n] = 'green'
                    elif val >= b_MPU and val <= b1_MPU:
                        cc[n] = 'lime'
                    elif val >= c_MPU and val <= c1_MPU:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 100., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 100., 50.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Maximum Push Up")
                plt.ylabel("Repetition")
                plt.ylim(xx, yy)
                PU1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_MPU) + ')')
                PU2 = mpatches.Patch(color='lime', label='Average (' + str(b_MPU) + '-' + str(b1_MPU) + ')')
                PU3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_MPU) + '-' + str(c1_MPU) + ')')
                PU4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_MPU) + ')')
                plt.legend(handles=[PU1, PU2, PU3, PU4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == '1 MIN SIT UP':
                x = df['NAME']
                y = round(df['1 MIN SIT UP'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_MSU = 1
                b_MSU = 2
                b1_MSU = 3
                c_MSU = 4
                c1_MSU = 5
                d_MSU = 6
                for n, val in enumerate(y):
                    if val < 10:
                        cc[n] = 'green'
                    elif val >= 11 and val < 25:
                        cc[n] = 'lime'
                    elif val >= 26 and val <= 35:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 100., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 100., 40.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("1 Minute Sit Up")
                plt.ylabel("Repetition")
                plt.ylim(xx, yy)
                SU1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_MSU) + ')')
                SU2 = mpatches.Patch(color='lime', label='Average (' + str(b_MSU) + '-' + str(b1_MSU) + ')')
                SU3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_MSU) + '-' + str(c1_MSU) + ')')
                SU4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_MSU) + ')')
                plt.legend(handles=[SU1, SU2, SU3, SU4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'SBJ':
                x = df['NAME']
                y = round(df['SBJ'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_SBJ = 195
                b_SBJ = 195
                b1_SBJ = 210
                c_SBJ = 211
                c1_SBJ = 228
                d_SBJ = 228
                for n, val in enumerate(y):
                    if val < a_SBJ:
                        cc[n] = 'green'
                    elif val >= b_SBJ and val <= b1_SBJ:
                        cc[n] = 'lime'
                    elif val >= c_SBJ and val <= c1_SBJ:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 400., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 400., 300.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Standing Broad Jump (SBJ)")
                plt.ylabel("Distance (cm)")
                plt.ylim(xx, yy)
                SBJ1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_SBJ) + ')')
                SBJ2 = mpatches.Patch(color='lime', label='Average (' + str(b_SBJ) + '-' + str(b1_SBJ) + ')')
                SBJ3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_SBJ) + '-' + str(c1_SBJ) + ')')
                SBJ4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_SBJ) + ')')
                plt.legend(handles=[SBJ1, SBJ2, SBJ3, SBJ4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'CMJ':
                x = df['NAME']
                y = round(df['CMJ'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_CMJ = 41
                b_CMJ = 41
                b1_CMJ = 44
                c_CMJ = 45
                c1_CMJ = 50
                d_CMJ = 50
                for n, val in enumerate(y):
                    if val < a_CMJ:
                        cc[n] = 'green'
                    elif val >= b_CMJ and val <= b1_CMJ:
                        cc[n] = 'lime'
                    elif val >= c_CMJ and val <= c1_CMJ:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 120., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 120., 70.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Counter Movement Jump (CMJ)")
                plt.ylabel("Height (cm)")
                plt.ylim(xx, yy)
                CMJ1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_CMJ) + ')')
                CMJ2 = mpatches.Patch(color='lime', label='Average (' + str(b_CMJ) + '-' + str(b1_CMJ) + ')')
                CMJ3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_CMJ) + '-' + str(c1_CMJ) + ')')
                CMJ4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_CMJ) + ')')
                plt.legend(handles=[CMJ1, CMJ2, CMJ3, CMJ4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'ILLINOIS/L' or y == 'ILLINOIS/R':
                x = df['NAME']
                x_axis = np.arange(len(x))
                y6 = round(df['ILLINOIS/L'].astype(float), 2)
                cc = ['colors'] * len(y6)
                a_AT = 18.3
                b_AT = 18.2
                b1_AT = 18.3
                c_AT = 16.2
                c1_AT = 18.1
                d_AT = 15.2
                d1_AT = 16.1
                e_AT = 15.2
                for n, val in enumerate(y6):
                    if val > a_AT:
                        cc[n] = 'green'
                    elif val >= b_AT and val <= b1_AT:
                        cc[n] = 'lime'
                    elif val >= c_AT and val <= c1_AT:
                        cc[n] = 'yellow'
                    elif val >= d_AT and val <= d1_AT:
                        cc[n] = 'darkgoldenrod'
                    else:
                        cc[n] = 'red'
                width = st.sidebar.slider("plot width", 1., 20., 15.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 20., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 40., 15.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x_axis - 0.2, y6, width=0.2, color=cc)
                for i in range(len(x)):
                    plt.text(i - 0.25, y6[i], y6[i], ha="left", va="bottom", fontsize="medium", rotation='vertical')
                y61 = round(df['ILLINOIS/R'].astype(float), 2)
                cc = ['colors'] * len(y61)
                for n, val in enumerate(y61):
                    if val > a_AT:
                        cc[n] = 'green'
                    elif val >= b_AT and val <= b1_AT:
                        cc[n] = 'lime'
                    elif val >= c_AT and val <= c1_AT:
                        cc[n] = 'yellow'
                    elif val >= d_AT and val <= d1_AT:
                        cc[n] = 'darkgoldenrod'
                    else:
                        cc[n] = 'red'

                ax = plt.bar(x_axis + 0.2, y61, width=0.2, color=cc)
                for i in range(len(x)):
                    plt.text(i + 0.25, y61[i], y61[i], ha="right", va="bottom", fontsize="medium", rotation='vertical')
                plt.xticks(x_axis, x, rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Illinois Agility Test (Left/Right)")
                plt.ylabel("Time (s)")
                plt.ylim(xx, yy)
                A1 = mpatches.Patch(color='green', label='Below Average > (' + str(a_AT) + ')')
                A2 = mpatches.Patch(color='lime', label='Average (' + str(b_AT) + '-' + str(b1_AT) + ')')
                A3 = mpatches.Patch(color='yellow', label='Normal (' + str(c_AT) + '-' + str(c1_AT) + ')')
                A4 = mpatches.Patch(color='darkgoldenrod', label='Above Average (' + str(d_AT) + '-' + str(d1_AT) + ')')
                A5 = mpatches.Patch(color='red', label='Excellent < (' + str(e_AT) + ')')
                plt.legend(handles=[A1, A2, A3, A4, A5], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'SIT & REACH':
                x = df['NAME']
                y = round(df['SIT & REACH'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_SR = 34
                b_SR = 34
                b1_SR = 39.5
                c_SR = 40
                c1_SR = 44
                d_SR = 44
                for n, val in enumerate(y):
                    if val < a_SR:
                        cc[n] = 'green'
                    elif val >= b_SR and val <= b1_SR:
                        cc[n] = 'lime'
                    elif val >= c_SR and val <= c1_SR:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 70., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 70., 40.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Modified Sit & Reach")
                plt.ylabel("Distance (cm)")
                plt.ylim(xx, yy)
                SR1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_SR) + ')')
                SR2 = mpatches.Patch(color='lime', label='Average (' + str(b_SR) + '-' + str(b1_SR) + ')')
                SR3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_SR) + '-' + str(c1_SR) + ')')
                SR4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_SR) + ')')
                plt.legend(handles=[SR1, SR2, SR3, SR4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == '10 M SPRINT':
                x = df['NAME']
                y = round(df['10 M SPRINT'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_10M = 1.86
                b_10M = 1.80
                b1_10M = 1.86
                c_10M = 1.73
                c1_10M = 1.79
                d_10M = 1.73
                for n, val in enumerate(y):
                    if val > a_10M:
                        cc[n] = 'green'
                    elif val >= b_10M and val <= b1_10M:
                        cc[n] = 'lime'
                    elif val >= c_10M and val <= c1_10M:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 5., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 5., 3.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("10 Meter Sprint")
                plt.ylabel("Time (s)")
                plt.ylim(xx, yy)
                S1 = mpatches.Patch(color='green', label='Below Average (>' + str(a_10M) + ')')
                S2 = mpatches.Patch(color='lime', label='Average (' + str(b_10M) + '-' + str(b1_10M) + ')')
                S3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_10M) + '-' + str(c1_10M) + ')')
                S4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (<' + str(d_10M) + ')')
                plt.legend(handles=[S1, S2, S3, S4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == '20 M SPRINT':
                x = df['NAME']
                y = round(df['20 M SPRINT'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_20M = 3.5
                b_20M = 3.28
                b1_20M = 3.5
                c_20M = 3.15
                c1_20M = 3.27
                d_20M = 3.15
                for n, val in enumerate(y):
                    if val > a_20M:
                        cc[n] = 'green'
                    elif val >= b_20M and val <= b1_20M:
                        cc[n] = 'lime'
                    elif val >= c_20M and val <= c1_20M:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 6., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 6., 5.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("20 Meter Sprint")
                plt.ylabel("Time (s)")
                plt.ylim(xx, yy)
                SS1 = mpatches.Patch(color='green', label='Below Average (>' + str(a_20M) + ')')
                SS2 = mpatches.Patch(color='lime', label='Average (' + str(b_20M) + '-' + str(b1_20M) + ')')
                SS3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_20M) + '-' + str(c1_20M) + ')')
                SS4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (<' + str(d_20M) + ')')
                plt.legend(handles=[SS1, SS2, SS3, SS4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == '40 M SPRINT':
                x = df['NAME']
                y = round(df['40 M SPRINT'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_40M = 3.5
                b_40M = 3.28
                b1_40M = 3.5
                c_40M = 3.15
                c1_40M = 3.27
                d_40M = 3.15
                for n, val in enumerate(y):
                    if val > a_40M:
                        cc[n] = 'green'
                    elif val >= b_40M and val <= b1_40M:
                        cc[n] = 'lime'
                    elif val >= c_40M and val <= c1_40M:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 15., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 15., 8.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("40 Meter Sprint")
                plt.ylabel("Time (s)")
                plt.ylim(xx, yy)
                SSS1 = mpatches.Patch(color='green', label='Below Average (>' + str(a_40M) + ')')
                SSS2 = mpatches.Patch(color='lime', label='Average (' + str(b_40M) + '-' + str(b1_40M) + ')')
                SSS3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_40M) + '-' + str(c1_40M) + ')')
                SSS4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (<' + str(d_40M) + ')')
                plt.legend(handles=[SSS1, SSS2, SSS3, SSS4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'TOTAL':
                x = df['NAME']
                y = round(df['TOTAL'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_HG = 71.7
                b_HG = 71.7
                b1_HG = 79.4
                c_HG = 79.5
                c1_HG = 89.4
                d_HG = 89.4
                for n, val in enumerate(y):
                    if val < a_HG:
                        cc[n] = 'green'
                    elif val >= b_HG and val <= b1_HG:
                        cc[n] = 'lime'
                    elif val >= c_HG and val <= c1_HG:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 150., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 150., 100.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Hand Grip Strength (Total)")
                plt.ylabel("Force (kg)")
                plt.ylim(xx, yy)
                HG1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_HG) + ')')
                HG2 = mpatches.Patch(color='lime', label='Average (' + str(b_HG) + '-' + str(b1_HG) + ')')
                HG3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_HG) + '-' + str(c1_HG) + ')')
                HG4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_HG) + ')')
                plt.legend(handles=[HG1, HG2, HG3, HG4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            elif y == 'YOYO TEST':
                x = df['NAME']
                y = round(df['YOYO TEST'].astype(float), 2)
                cc = ['colors'] * len(y)
                a_YY = 8.01
                b_YY = 8.01
                b1_YY = 9.11
                c_YY = 10.01
                c1_YY = 12.12
                d_YY = 12.12
                for n, val in enumerate(y):
                    if val < a_YY:
                        cc[n] = 'green'
                    elif val >= b_YY and val <= b1_YY:
                        cc[n] = 'lime'
                    elif val >= c_YY and val <= c1_YY:
                        cc[n] = 'yellow'
                    else:
                        cc[n] = 'darkgoldenrod'
                width = st.sidebar.slider("plot width", 1., 15., 10.)
                height = st.sidebar.slider("plot height", 1., 10., 5.)
                xx = st.sidebar.slider("bottom Y-axis", 0., 20., 0.)
                yy = st.sidebar.slider("upper Y-axis", 0., 20., 15.)
                fig, ax = plt.subplots(figsize=(width, height))
                ax = plt.bar(x, y, color=cc, width=0.5)
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha="center", va="bottom", fontsize="medium")
                plt.xticks(rotation='vertical', fontsize="medium", ha="right", va="center", wrap=True)
                plt.title("Yoyo Endurance Test")
                plt.ylabel("Level:Round")
                plt.ylim(xx, yy)
                YY1 = mpatches.Patch(color='green', label='Below Average (<' + str(a_YY) + ')')
                YY2 = mpatches.Patch(color='lime', label='Average (' + str(b_YY) + '-' + str(b1_YY) + ')')
                YY3 = mpatches.Patch(color='yellow', label='Above Average (' + str(c_YY) + '-' + str(c1_YY) + ')')
                YY4 = mpatches.Patch(color='darkgoldenrod', label='Excellent (>' + str(d_YY) + ')')
                plt.legend(handles=[YY1, YY2, YY3, YY4], bbox_to_anchor=(1, 1.3))
                st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)  # erase the warning

            else:
                x = df['NAME']
                y = round(df[y], 2)
                bar_value = fig = go.Figure(data=[go.Bar(x=x, y=y, text=y, textposition='auto')])
                st.plotly_chart(bar_value)
            return

        load_data(y_value)
