import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt



def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Body Mechanics", "Gym Attendance","Supplement"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
       st.header("Home Page")
       username = st.sidebar.text_input("Username")
       password = st.sidebar.text_input("Password", type='password')
       if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password"] and username == st.secrets["username"]:
                components.html(""" 
                 <h1 style = "color:yellow; background-color:blue" >Welcome to Sports Science & Sports Medicine</h1>
                 <p><h2 style = "color:black";>Aim</h2></p>
                 <p><h3 style = "color:orange";>Improve athlete's performance is our mission</h3></p>   
                 """,scrolling=False)             
                image = Image.open('ussps.jpg')
                st.image(image, caption='Photo with intership students')
                st.video('https://www.youtube.com/watch?v=iRAKIcJ_9HM&list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                st.video('https://youtu.be/Kz0Y5ZT119I?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD') 
                st.video('https://youtu.be/pcSARMfV9z4?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                 
               
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
       if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password"]:
                   sheet_id = st.secrets[username]
                   df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
                   chosen = df.rename(columns={'Month': 'Total Cases'})
                   a = chosen.groupby(['Year'])['Total Cases'].count()
                   table_in_year = chosen.groupby(['Year'],sort=False,as_index=False)['Total Cases'].count()
                   col1, col2 = st.columns(2)   
                   col1.table(table_in_year)
                   x1 = df['Year'].drop_duplicates()
                   y1 = a
                   fig, ax = plt.subplots(nrows=1, ncols=1)   
                   ax.plot(x1,y1, marker='^', color='blue', mec='red', ls='--')
                   ax.set_title("Bodymechanics Service")
                   ax.set_xlabel('Year')
                   ax.set_ylabel('Case')
                   col2.pyplot(fig)
                   
                                
                   year = st.selectbox('Chose The Year', df['Year'].drop_duplicates())
                   col1, col2 = st.columns(2)
                   selected_year = df.loc[df['Year'] == year]
                   selected = selected_year.rename(columns={'Name': 'Case'})
                   b= selected.groupby(['Month'], sort=False,as_index=False)['Case'].count()
                   y= selected.groupby(['Month'], sort=False)['Case'].count()
                   x = selected['Month'].drop_duplicates()
                   col1.table(b)
                   fig, ax = plt.subplots(nrows=1, ncols=1)   
                   ax.plot(x,y, marker='o', color='blue', mec='red', ls=':')
                   ax.set_title("Cases in year " + year)
                   ax.set_xlabel('Month')
                   ax.set_ylabel('Case')
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
                   
                
                   st.subheader('Cases by Gender & Status' + '(' +month +'/'+year+')')    
                   color =  ["green", "red"]
                   ax[0].pie(y1,labels=y1, colors = color, autopct='%1.1f%%' )
                   ax[1].pie(y2,labels=y2, autopct='%1.1f%%')
                   ax[0].legend(p2, loc='best')
                   ax[1].legend(p3, loc='best')
                   fig.tight_layout()
                   st.pyplot(fig)
                   
                   st.subheader('Cases by Sports' + '(' +month +'/'+year+')') 
                   fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))    
                   ax.pie(y,labels=y, autopct='%1.1f%%', pctdistance=1.1, labeldistance= 0.6, textprops={'fontsize': 8})
                   ax.legend(p1, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                   fig.tight_layout()
                   st.pyplot(fig)
                    
                    
                   st.subheader('Cases by Patient' + '(' +month +'/'+year+')') 
                   fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))    
                   ax.pie(y3,labels=y3)
                   ax.legend(p4, loc='best', bbox_to_anchor=(1.05, 1.0), fontsize='xx-small')
                   fig.tight_layout()
                   st.pyplot(fig)   
                
                
                   st.subheader(' Sports' + '('+year+')')
                   sport = st.selectbox('Chose The Sport', df['Sport'].drop_duplicates())  
                   replaceG = selected_year.loc[df['Sport'] == sport]
                   chosen_sport = replaceG.rename(columns={'Gender': 'Case'})
                   cs = chosen_sport.groupby(['Month','Name'],sort=False, as_index=False)['Case'].count()
                   st.table(cs)
                   athlete = st.selectbox('Chose Athlete', chosen_sport['Name'].drop_duplicates())
                   replaceG1 = chosen_sport.loc[df['Name'] == athlete]
                   chosen_athlete = replaceG1.rename(columns={'Gender': 'Case'})
                   ca = chosen_athlete.groupby(['Month','Injury Part'],sort=False, as_index=False)['Case'].count()
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
                    period = (df['DATE'] >= startdate) & (df['DATE'] <= enddate)
                    wholedata = df.loc[period]
                    st.write(wholedata)
                    bysport = wholedata.groupby(['DATE'])['SPORT'].count()
                    bygender = wholedata.groupby(['DATE'])['GENDER'].count()
                    bystatus = wholedata.groupby(['DATE'])['STATUS'].count()
                    bydate = wholedata.groupby(['DATE'])['GENDER'].count()
                    st.write(bysport)
                    st.write(bygender)
                    st.write(bystatus)
    
    
    
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
                    
                 

                    


if __name__ == '__main__':
    main()

