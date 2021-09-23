import streamlit as st
from Multi_Page_App import MultiApp
from APP import Home_Page, Second_Page

st.beta_set_page_config(page_title='Bar Chart Maker')

app = MultiApp()

st.title('Fitness Test Web Application')

app.add_app("Bar Chart Maker", Home_Page.app)
app.add_app("Bar Chart Maker (Data Comparison)", Second_Page.app)

app.run()

