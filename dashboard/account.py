import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
#<------------------Database Connection-------------------------------->
cred = credentials.Certificate('logiplacement-fa36826924e2.json')
#firebase_admin.initialize_app(cred)

#<---------------------------------------------------------------------->
def app():
    
    
    with open('design.css') as source_des:
        st.markdown(f"<style>{source_des.read()}",unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: centre;'>Welcome To LogiPlacement </h1> ",unsafe_allow_html=True)
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():
        try: 
            user = auth.get_user_by_email(email)
            st.write('Login Successful') 
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.signedout = True
            st.session_state.signout = True  

        except:
            st.warning("Login Failed")

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

#<----------------------------------------------------------------------->
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False


    if not st.session_state['signout']:
        choice = st.selectbox("Login / SignUp", ['Login','Sign Up'])



        if choice == "Login":
            email =  st.text_input('Email Address')
            password = st.text_input('Password', type= 'password')

            st.button('Login',on_click=f)



        else:
            name = st.text_input('Name')
            surname = st.text_input('Surname')
            username = st.text_input('UserName')
            email =  st.text_input('Email Address')
            password = st.text_input('Password', type= 'password')
            age = st.slider('How old are you?', 0, 100, 25)
            st.write("I'm ", age, 'years old')

            if st.button('Create Account'):
                user = auth.create_user(email = email,password = password, uid = username)

                st.success('Account created successfully!')
                st.markdown("Please Login using your email and password")
                st.balloons()


#<------------------------------------------------------------------------------->       
    if st.session_state.signout:
        st.text('Name '+st.session_state.username)
        st.text('Email id: '+st.session_state.useremail)
        st.button('Sign out', on_click=t)
