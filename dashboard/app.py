import streamlit as st

from streamlit_option_menu import option_menu


import home, Placement, about, account, resume,Aptitude_Time
st.set_page_config(
        page_title="LogiPlacement",
)

hide_st_style = """<style>  footer {visibility: hidden;}</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='LogiPlacement ',
                options=['Home','Account','Placement','Resume','Aptitude Time','About'],
                icons=['house-fill','person-circle','bi-graph-up-arrow','file-earmark-person-fill','vector-pen','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "Placement":
            Placement.app()        
        if app == 'Resume':
            resume.app()
        if app == 'Aptitude Time':
            Aptitude_Time.app()  
        if app == 'About':
            about.app()    
             
          
             
    run()