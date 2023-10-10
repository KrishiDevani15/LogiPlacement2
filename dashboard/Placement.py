import streamlit as st
import numpy as np
import pickle


def place_prediction(data):
    model = pickle.load(open('E:/apps/dashboard/Lr.pkl', 'rb'))
    val = model.predict([data])

    res = val[0]/100
    print(res)
    val_str = ''
    if res < 50:
        res = str(res)
        val_str = "You need to prepare well!!"
    
    elif res >49:
        res = str(res)
        val_str = "All the very best, you are doing well!! Your placement chances are" + res + "%"
    
    else:
        val_str = "Something went wrong! Try again later."
    

def app():
    
    st.write("Hello")
    
    Coding_Skills = st.text_input("Enter Coding Skills")
    Aptitude_Skills= st.text_input("Enter Aptitude Skills  ")
    Technical_Skills = st.text_input("Enter Technical Skills ")
    Communication_Skills = st.text_input("Enter Communication Skills ")
    Core_Knowledge = st.text_input("Enter Core Knowledge ")
    Presentation_Skills = st.text_input("Enter Presentation Skills ")
    Academic_Performance = st.text_input("Enter Academic Performance ")
    Puzzle_Solving_skills = st.text_input("Enter Puzzle Solving skills ")
    English_Proficiency = st.text_input("Enter English_Proficiency ")
    Programming_Skills = st.text_input("Enter Programming_Skills ")
    Management_Skills = st.text_input("Enter Management_Skills ")
    Projects = st.text_input("Enter Number of Projects ")
    Internships = st.text_input("Enter Internships ")
    Training = st.text_input("Enter Training ")
    Backlog = st.text_input("Enter Coding ")

    Placement = ''

    if st.button('Placed test result'):
        Placement = place_prediction([[Coding_Skills,Aptitude_Skills,Technical_Skills ,Communication_Skills,Core_Knowledge,Presentation_Skills,Academic_Performance,Puzzle_Solving_skills,English_Proficiency,Programming_Skills,Management_Skills,Projects,Internships,Training,Backlog]])
    st.success(Placement)


if __name__ == "__main__":
    app()

