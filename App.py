import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
   page_title="Sports Science & Sports Medicine",
   page_icon="msnpp.png",
   layout="wide",
   initial_sidebar_state="expanded",)


def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Body Mechanics", "Gym Attendance","Supplement","Sports Rehab"]
    st.sidebar.image('msnpp.png')
    choice = st.sidebar.selectbox("Menu",menu)
      
    if choice == "Home":
       st.header("Home Page")
       col1, col2, col3, col4, col5 = st.columns(5) 
       image_1 = Image.open('penang.png')
       image_2 = Image.open('blackpanther.png')
       image_3 = Image.open('msnpp.png')
       image_4 = Image.open('penang2030.png')
       image_5 = Image.open('sportforall.png')
       col3.image(image_1, caption='Penang State Logo')
       col4.image(image_2, caption='Penang Black Panther')
       col2.image(image_3, caption='MSN Logo')
       col5.image(image_4, caption='Penang 2030 Logo')
       col1.image(image_5, caption='Logo Sports For All')
       username = st.sidebar.text_input("Username")
       password = st.sidebar.text_input("Password", type='password')
       if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password"] and username == st.secrets["username"]:            
                image = Image.open('ussps.jpg')
                st.image(image, caption='Photo with intership students')
                st.subheader('Nutrition Education Video')
                col1, col2, col3 = st.columns(3) 
                col1.video('https://www.youtube.com/watch?v=iRAKIcJ_9HM&list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                col2.video('https://youtu.be/Kz0Y5ZT119I?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD') 
                col3.video('https://youtu.be/pcSARMfV9z4?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                 
               
            else:
                st.warning("Incorrect username/password")
        
    elif choice == "Data Analysis":
        st.header("Data Analysis Section")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password_1"] and username == st.secrets["username_1"]:
                    app = MultiApp()
                    st.title('Fitness Test Web Application')
                    app.add_app("Bar Chart Maker", Home_Page.app)
                    app.add_app("Bar Chart Maker (Data Comparison)", Second_Page.app)
                    app.run()

        




            else:
                st.warning("Incorrect username/password")

    elif choice == "Body Mechanics":
       st.header("Body Mechanics Section")
       username = st.sidebar.text_input("Username")
       password = st.sidebar.text_input("Password", type='password')
       col1, col2, col3, col4 = st.columns(4) 
       image_1 = Image.open('msnppbodymec1.PNG')
       image_2 = Image.open('msnppbodymec2.PNG')
       image_3 = Image.open('msnppbodymec3.PNG')
       image_4 = Image.open('msnppbodymec4.PNG')
       col1.image(image_1)
       col2.image(image_2)
       col3.image(image_3)
       col4.image(image_4)
       st.video('bodymec(TNT).mp4')
       if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password"]:
                   sheet_id = st.secrets[username]
                   df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
                   chosen = df.rename(columns={'Month': 'Total Usage'})
                   a = chosen.groupby(['Year'])['Total Usage'].count()
                   table_in_year = chosen.groupby(['Year'],sort=False,as_index=False)['Total Usage'].count()
                   col1, col2 = st.columns(2)   
                   col1.table(table_in_year)
                   x1 = df['Year'].drop_duplicates()
                   y1 = a
                   fig, ax = plt.subplots(nrows=1, ncols=1)   
                   ax.plot(x1,y1, marker='^', color='blue', mec='red', ls='--')
                   ax.set_title("Bodymechanics Service")
                   ax.set_xlabel('Year')
                   ax.set_ylabel('Usage')
                   col2.pyplot(fig)
                   
                                
                   year = st.selectbox('Chose The Year', df['Year'].drop_duplicates())
                   col1, col2 = st.columns(2)
                   selected_year = df.loc[df['Year'] == year]
                   selected = selected_year.rename(columns={'Name': 'Usage'})
                   b= selected.groupby(['Month'], sort=False,as_index=False)['Usage'].count()
                   y= selected.groupby(['Month'], sort=False)['Usage'].count()
                   x = selected['Month'].drop_duplicates()
                   col1.table(b)
                   fig, ax = plt.subplots(nrows=1, ncols=1)   
                   ax.plot(x,y, marker='o', color='blue', mec='red', ls=':')
                   ax.set_title("Cases in year " + year)
                   ax.set_xlabel('Month')
                   ax.set_ylabel('Usage')
                   col2.pyplot(fig)
                    
                   month = st.selectbox('Chose The Month', df['Month'].drop_duplicates())       
                   selected_month = selected_year.loc[df['Month'] == month]
                   st.write(selected_month)
                   fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 6))   
                   y = selected_month.groupby(['Sport'])['Month'].count()
                   p1 = selected_month.groupby('Sport').groups
                   y1 = selected_month.groupby(['Gender'])['Month'].count()
                   p2 = selected_month.groupby('Gender').groups
                   y2 = selected_month.groupby(['Status'])['Month'].count()
                   p3 = selected_month.groupby('Status').groups
                   y3 = selected_month.groupby(['Name'])['Month'].count()
                   p4 = selected_month.groupby('Name').groups
                   
                
                   st.subheader('Usage by Gender & Status' + '(' +month +'/'+year+')')    
                   color =  ["green", "red"]
                   ax[0].pie(y1,labels=y1, colors = color, autopct='%1.1f%%' )
                   ax[1].pie(y2,labels=y2, autopct='%1.1f%%')
                   ax[0].legend(p2, loc='best')
                   ax[1].legend(p3, loc='best')
                   fig.tight_layout()
                   st.pyplot(fig)
                   
                   st.subheader('Usage by Sports' + '(' +month +'/'+year+')') 
                   fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))    
                   ax.pie(y,labels=y, autopct='%1.1f%%', pctdistance=1.1, labeldistance= 0.6, textprops={'fontsize': 8})
                   ax.legend(p1, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                   fig.tight_layout()
                   st.pyplot(fig)
                    
                    
                   st.subheader('Usage by Patient' + '(' +month +'/'+year+')') 
                   fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))    
                   ax.pie(y3,labels=y3)
                   ax.legend(p4, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                   fig.tight_layout()
                   st.pyplot(fig)   
                
                
                   st.subheader(' Sports' + '('+year+')')
                   sport = st.selectbox('Chose The Sport', df['Sport'].drop_duplicates())  
                   replaceG = selected_year.loc[df['Sport'] == sport]
                   chosen_sport = replaceG.rename(columns={'Gender': 'Usage'})
                   chosen_sport2 = replaceG.rename(columns={'Name': 'Usage'})
                   chosen_sport3 = replaceG.rename(columns={'Gender': 'Cost(RM)'})
                   chosen_sport4 = replaceG.rename(columns={'Gender': 'Usage'})
                   cs2 = chosen_sport2.groupby(['Month'],sort=False)['Usage'].count()
                   cs3 = chosen_sport4.groupby(['Name'])['Usage'].count()
                   cs4 = chosen_sport3.groupby(['Name'])['Cost(RM)'].count()
                   x_axis = replaceG['Month'].drop_duplicates()
                   fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(6, 4))   
                   ax.plot(x_axis,cs2, marker='^', color='blue', mec='red', ls='--')
                   ax.set_title(sport + " ("+ year+")")
                   ax.set_xlabel('Month')
                   ax.set_ylabel('Usage (Per Entry)')
                   st.pyplot(fig)
                   st.bar_chart(cs3)
                   paid = cs4 * 100
                   st.subheader("Total Cost (RM)")
                   st.table(paid)

   
                  
                   athlete = st.selectbox('Chose Athlete', chosen_sport['Name'].drop_duplicates())
                   replaceG1 = chosen_sport.loc[df['Name'] == athlete]
                   chosen_athlete = replaceG1.rename(columns={'Gender': 'Usage'})
                   ca = chosen_athlete.groupby(['Month','Injury Part'],sort=False, as_index=False)['Usage'].count()
                   ca1 = chosen_athlete.groupby(['Month'],sort=False)['Usage'].count()
                   x_axis1 = replaceG1['Month'].drop_duplicates()
                   fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(6, 4))   
                   ax.plot(x_axis1,ca1, marker='^', color='blue', mec='red', ls='--')
                   ax.set_title(athlete + " ("+ year+")")
                   ax.set_xlabel('Month')
                   ax.set_ylabel('Usage (Per Entry)')
                   st.pyplot(fig)
                   st.table(ca)
                   
    
    elif choice == "Gym Attendance":
          st.header("Gym Attendance Section")
          username = st.sidebar.text_input("Username")
          password = st.sidebar.text_input("Password", type='password')
          if st.sidebar.checkbox("Login"): 
               if password == st.secrets["password"]:
                    sheet_id = st.secrets[username]
                    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='Attendance')
                    col1, col2 = st.columns(2)
                    startdate = col1.text_input("Chose the start date(year/month/day):")
                    enddate = col2.text_input("Chose the end date(year/month/day):")
                    df['DATE'] = pd.to_datetime(df['DATE'], format="%d/%m/%Y")
                    year = df['DATE'].dt.day_name()
                    year_2 = df['DATE'].dt.day_name()
                    period = (df['DATE'] >= startdate) & (df['DATE'] <= enddate)
                    wholedata = df.loc[period]
                    
                    bysport = wholedata.groupby(['SPORT'])['NAME'].count()
                    bygender = wholedata.groupby(['GENDER'])['NAME'].count()
                    bystatus = wholedata.groupby(['STATUS'])['NAME'].count()
                    bydate_2 = wholedata.rename(columns={'NAME': 'USAGE'})
                    bydate = bydate_2.groupby(['DATE'])['USAGE'].count()
                    byday = wholedata.groupby([year])['NAME'].count()
                    legend_type = wholedata.groupby('SPORT').groups
                    legend_type_2 = wholedata.groupby('GENDER').groups
                    legend_type_3 = wholedata.groupby('STATUS').groups
                    legend_type_4 = wholedata.groupby('DATE').groups
                    legend_type_5 = wholedata.groupby(year).groups
                    st.subheader("Total usage from "+startdate+" to "+enddate)
                    st.line_chart(bydate)
                    
                    fig, ax = plt.subplots(nrows=1, ncols=1)    
                    ax.pie(bysport,labels=bysport, autopct='%1.1f%%', pctdistance=1.1, labeldistance= 0.8, textprops={'fontsize': 8})             
                    ax.legend(legend_type, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')                 
                    ax.set_title("Total usage (Sport)"+ "\nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    
                    fig, ax = plt.subplots(nrows=1, ncols=2)    
                    ax[0].pie(bygender,labels=bygender, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[1].pie(bystatus,labels=bystatus, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[0].legend(legend_type_2, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[1].legend(legend_type_3, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[0].set_title("Total usage (Gender)"+ "\nfrom "+startdate+" to "+enddate)
                    ax[1].set_title("Total usage (Status)"+ "\nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    
                    fig, ax = plt.subplots(nrows=1, ncols=1)    
                    ax.pie(byday,labels=byday, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax.legend(legend_type_5, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax.set_title("Total usage (Day)"+ "\nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    
                    
                    select_sport = st.selectbox('Chose the sport', legend_type)
                    chosen = wholedata.loc[df['SPORT'] == select_sport]
                    chosen_2 = chosen.rename(columns={'DATE': 'USAGE'})
                    chosen_sport = chosen_2.groupby(['NAME'])['USAGE'].count()
                    st.subheader("Total usage by "+select_sport+ " from "+startdate+" to "+enddate)
                    st.bar_chart(chosen_sport)
                    datedetail = chosen[['DATE','NAME','GENDER','AGE','STATUS']]
                    st.write(datedetail)
    
    
    elif choice == "Supplement":
          st.header("Supplement Section")
          username = st.sidebar.text_input("Username")
          password = st.sidebar.text_input("Password", type='password')
          if st.sidebar.checkbox("Login"): 
               if password == st.secrets["password"]:
                    sheet_id = st.secrets[username]
                    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='Sheet1')
                    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
                    col1, col2 = st.columns(2)
                    startdate = col1.text_input("Chose the start date(year/month/day):")
                    enddate = col2.text_input("Chose the end date(year/month/day):")
                    mask = (df['Date'] >= startdate) & (df['Date'] <= enddate)
                    wholedata = df.loc[mask]
                    st.write(wholedata)
                    
                    supplement_type = wholedata.groupby(['Supplement'])['Quantity'].sum()   
                    total_price = wholedata.groupby(['Supplement'])['Total Price (RM)'].sum()
                    sport = wholedata.groupby(['Sports','Supplement'])['Quantity','Total Price (RM)'].sum()
                    gender = wholedata.groupby(['Gender'])['Quantity'].sum()
                    purpose = wholedata.groupby(['Purpose'])['Quantity'].sum()                                    
                    sport_quantity = wholedata.groupby(['Sports'])['Quantity'].sum()
                    sport_quantity_2 = wholedata.groupby(['Sports'])['Total Price (RM)'].sum()
                    
                    legend_type = wholedata.groupby('Supplement').groups
                    legend_type_2 = wholedata.groupby('Sports').groups
                    legend_type_3= wholedata.groupby('Gender').groups
                    legend_type_4 = wholedata.groupby('Purpose').groups                                        
                                                             
                 

                    fig, ax = plt.subplots(nrows=1, ncols=2)    
                    ax[0].pie(supplement_type,labels=supplement_type, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[1].pie(total_price,labels=total_price, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[0].legend(legend_type, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[1].legend(legend_type, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[0].set_title("Total amount of supplement given \n(unit) "+ "\nfrom "+startdate+" to "+enddate)
                    ax[1].set_title("Total value of supplement \n(RM)"+ "\nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    
                    fig, ax = plt.subplots(nrows=1, ncols=2)    
                    ax[0].pie(gender,labels=gender, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[1].pie(purpose,labels=purpose, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[0].legend(legend_type_3, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[1].legend(legend_type_4, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[0].set_title("Total amount of supplement given \n(gender) "+ "\nfrom "+startdate+" to "+enddate)
                    ax[1].set_title("Total amount of supplement given \n(purpose) "+ "\nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    
                    
                    
                    fig, ax = plt.subplots(nrows=1, ncols=2)    
                    ax[0].pie( sport_quantity,labels= sport_quantity, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[1].pie(sport_quantity_2,labels=sport_quantity_2, autopct='%1.1f%%', pctdistance=1.2, labeldistance= 0.6, textprops={'fontsize': 8})
                    ax[0].legend(legend_type_2, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[1].legend(legend_type_2, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                    ax[0].set_title("Sports that given supplement (unit)"+ " \nfrom "+startdate+" to "+enddate)
                    ax[1].set_title("Sports that given supplement (RM)"+ " \nfrom "+startdate+" to "+enddate)
                    fig.tight_layout()
                    st.pyplot(fig)
                    st.subheader("Sports that given supplement"+ " from "+startdate+" to "+enddate)
                    st.write(sport)
                    
                    sportchosen = st.selectbox('Chose the sport', wholedata['Sports'].drop_duplicates())
                    selectedsport = wholedata.loc[df['Sports']==sportchosen]
                    filtersport = selectedsport.groupby(['Supplement','Name'])['Quantity','Total Price (RM)'].sum()
                    st.subheader("Supplement taken by "+sportchosen+ " ("+startdate+" to "+enddate+")")
                    st.write(filtersport)
                 
    
    
    elif choice == "Sports Rehab":
          st.header("Sports Rehabilitation Section")
          username = st.sidebar.text_input("Username")
          password = st.sidebar.text_input("Password", type='password')
          if st.sidebar.checkbox("Login"): 
               if password == st.secrets["password"]:
                    sheet_id = st.secrets[username]
                    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='Database')
                    df1 = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='Database1')
                    df['DATE'] = pd.to_datetime(df['DATE'], '%Y/%m/%d')
                    df1['DATE'] = pd.to_datetime(df1['DATE'], '%Y/%m/%d')
                    col1, col2 = st.columns(2)
                    startdate = col1.text_input("Chose the start date(year/month/day):")
                    enddate = col2.text_input("Chose the end date(year/month/day):")
                    period = (df['DATE'] >= startdate) & (df['DATE'] <= enddate) 
                    period_2 = (df1['DATE'] >= startdate) & (df1['DATE'] <= enddate) 
                    selected_period = df.loc[period]
                    selected_1 = selected_period[['DATE','NAME','GENDER','STATUS','SPORT','INJURY PART_1','INJURY PART_2','FINDING','ACTION']]
                    selected_period_2 = df1.loc[period_2]
                    st.subheader("Assessment and Treatment ("+"from "+startdate+" to "+enddate+")")
                    st.write(selected_1)
                    st.subheader("Rehabilitation ("+"from "+startdate+" to "+enddate+")")
                    st.write(selected_period_2)
                    st.subheader("Injury Report ("+"from "+startdate+" to "+enddate+")")
                    selectperiod = selected_period.sort_values(by=['SPORT'], inplace=False, ignore_index=True)
                    chosen_sport = st.selectbox('Chose The Sport', selectperiod['SPORT'].drop_duplicates())
                    sport = selected_period.loc[df['SPORT']==chosen_sport]
                    selected_sport = sport[['DATE','NAME','GENDER','STATUS','INJURY PART_1','INJURY PART_2','FINDING','ACTION']]
                    st.write(selected_sport)
                    st.download_button(label='Download the dataframe',data=selected_sport.to_csv(),mime='text/csv', file_name='Injury Report.csv')
                    sport['combine'] = sport['INJURY PART_1'] +''+ sport['INJURY PART_2']
                    st.write(sport)




if __name__ == '__main__':
    main()

