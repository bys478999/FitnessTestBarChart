import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page


def main():
    st.title("Simple Login App")
    menu = ["Home","Login","Sign Up"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"): 
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

