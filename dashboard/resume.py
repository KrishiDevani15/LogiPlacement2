import streamlit as st
import time

def app():
    st.snow()
    col1,col2,col3  = st.columns([1,2,1])
    col1.markdown("# Upload your :violet[Resume] ")
    col1.markdown(" Here your can examine your resume with others. ")
    upload_resume = col2.file_uploader("Upload your Resume")
    camera_resume = col2.camera_input("Take a Resume photo")
    progress_bar = col2.progress(0)

    for perc_completed in range(100):
       #time.sleep(0.01)
       progress_bar.progress(perc_completed+1)
    col2.success('Photo uploaded sucessfully')