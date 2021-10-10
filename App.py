import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image




def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Service"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.header("Home Page")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"): 
            if password == '123' and username == 'abu':
                components.html(""" 
                 <h1 style = "color:yellow; background-color:blue" >Welcome to Sports Science & Sports Medicine</h1>
                 <p><h2 style = "color:black";>Aim</h2></p>
                 <p><h3 style = "color:orange";>Improve athlete's performance is our mission</h3></p>   
                 """,scrolling=False)             
                image = Image.open('ussps.jpg')
                st.image(image, caption='Photo with intership students')
                st.video('https://youtu.be/iRAKIcJ_9HM?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                st.video('https://youtu.be/Kz0Y5ZT119I?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD') 
                st.video('https://youtu.be/pcSARMfV9z4?list=PLNU1HqjHb92rscpN1h-HflhQRaunwDFbD')
                 
               
            else:
                st.warning("Incorrect username/password")
        
    elif choice == "Data Analysis":
        st.header("Data Analysis Section")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"): 
            if password == '1234' and username == 'abu':
                    app = MultiApp()
                    st.title('Fitness Test Web Application')
                    app.add_app("Bar Chart Maker", Home_Page.app)
                    app.add_app("Bar Chart Maker (Data Comparison)", Second_Page.app)
                    app.run()

        




            else:
                st.warning("Incorrect username/password")

    elif choice == "Service":
        st.header("Our Service")

if __name__ == '__main__':
    main()

