import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt



def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Body Mechanics", "Sports Rehab"]
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
       username = st.sidebar.text_input("Username")
       password = st.sidebar.text_input("Password", type='password')
       if st.sidebar.checkbox("Login"): 
            if password == st.secrets["password"]:
                   sheet_id = st.secrets[username]
                   st.header("Body Mechanics Service")
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
                   y1 = selected_month.groupby(['Gender'])['Month'].count()
                   y2 = selected_month.groupby(['Status'])['Month'].count()
                   mylabels = selected_month['Sport'].drop_duplicates()
                   mylabels1 = selected_month['Gender'].drop_duplicates()
                   mylabels2 = selected_month['Status'].drop_duplicates()
                   st.subheader('Cases by Gender & Status' + '(' +month +'/'+year+')')    
                   color =  ["green", "red"]
                   ax[0].pie(y1,labels=y1, colors = color )
                   ax[1].pie(y2,labels=y2)
                   ax[0].legend(mylabels1, loc='best')
                   ax[1].legend(mylabels2, loc='best')
                   fig.tight_layout()
                   st.pyplot(fig)
                   
                   st.subheader('Cases by Sports' + '(' +month +'/'+year+')') 
                   fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))    
                   ax.pie(y,labels=y)
                   ax.legend(mylabels, loc='best', bbox_to_anchor=(1.05, 1.0))
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
                   
    elif choice == "Sports Rehab":
          username = st.sidebar.text_input("Username")
          password = st.sidebar.text_input("Password", type='password')
          if st.sidebar.checkbox("Login"): 
               if password == st.secrets["password"]:
                    sheet_id = st.secrets[username]
                    st.header("Sports Rehab Service")
                    df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='Database')
                    df1 = df.rename(columns={'NAME': 'COUNT'})
                    a = df1.groupby(['IC NUMBER','COUNT','STATUS'])['COUNT'].count()
                    st.write(a)
                    df1.add_rows(a)
                  
                  
                   

                    


if __name__ == '__main__':
    main()

