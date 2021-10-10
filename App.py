import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page
import streamlit.components.v1 as components
from PIL import Image




def main():
    st.title("""Sports Science & Sports Medicine Website""")
    menu = ["Home","Data Analysis","Sign Up"]
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
                components.html(""" 
                 <h1 style = "color:yellow; background-color:blue" >Welcome to Sports Science & Sports Medicine</h1>
                 <p><h2 style = "color:black";>Aim</h2></p>
                 <p><h3 style = "color:orange";>Improve athlete's performance is our mission</h3></p>   
                 """,scrolling=False)    
                components.html(""" 
                 <iframe src="https://www.youtube.com/watch?v=7wtfhZwyrcc" title="Imagine Dragons - Believer"></iframe>
                 """,scrolling=False) 
                st.markdown('Our Aim:')
                st.markdown("Improve athlete's performance is our mission")
                image = Image.open('ussps.jpg')
                st.image(image, caption='Photo with intership students')
               
            else:
                st.warning("Incorrect username/password")
        
    elif choice == "Data Analysis":
        st.subheader("Data Analysis Section")
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

    elif choice == "Sign Up":
        st.subheader("Create New Account")

if __name__ == '__main__':
    main()

