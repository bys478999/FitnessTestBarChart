import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Service"]
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

    elif choice == "Service":
       username = st.sidebar.text_input("Username")
       password = st.sidebar.text_input("Password", type='password')
       if st.sidebar.checkbox("Login"): 
            if password == "1234" and username == "abu":
                   sheet_id = '1NVPrXAes46nxhhevFzuvRkUCM9Y6JQNqUteR9KUyL-I'
                   st.header("BodyMechanics Service")
                   df = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
                   st.dataframe(df)  
                   a= df.groupby(['Year'])['Month'].count()
                   col11, col22 = st.columns(2)   
                   col11.write(a)
                   x1 = df['Year']
                   y1 = a
                   fig1, ax = plt.subplots(nrows=1, ncols=1)   
                   ax.plot(x1,y1)
                   ax.set_title("Bodymechanics Service")
                   ax.set_xlabel('Year')
                   ax.set_ylabel('Case')
                   col22.pyplot(fig1)
                   
                                
                   year = st.selectbox('Chose The Year', df['Year'].drop_duplicates())
                   col1, col2 = st.columns(2)
                   selected_year = df.loc[df['Year'] == year]
                   selected = selected_year.rename(columns={'Name': 'Case'})
                   b= selected.groupby(['Month'])['Case'].count()
                   x = selected['Month'].drop_duplicates()
                   col1.table(b)
                   fig, ax = plt.subplots(nrows=1, ncols=1)   
                   y = b
                   ax.plot(x,y)
                   ax.set_title("Cases in year " + year)
                   ax.set_xlabel('Month')
                   ax.set_ylabel('Case')
                   col2.pyplot(fig)
                    
               
                    
                    


if __name__ == '__main__':
    main()

