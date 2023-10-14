from flask import Flask, request, render_template
import numpy as np
import model
import pickle

app = Flask(__name__,template_folder="templates")
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    
    Coding_Skills = request.args.get('Coding_Skills')
    Aptitude_Skills = request.args.get('Aptitude_Skills')
    Technical_Skills = request.args.get('Technical_Skills')
    Communication_Skills= request.args.get('Communication_Skills')
    Core_Knowledge = request.args.get('Core_Knowledge')
    Presentation_Skills = request.args.get('Presentation_Skills')
    Academic_Performance = request.args.get('Academic_Performance')
    Puzzle_Solving_skills = request.args.get('Puzzle_Solving_skills')
    English_Proficiency = request.args.get('English_Proficiency')
    Programming_Skills = request.args.get('Programming_Skills')
    Management_Skills = request.args.get('Management_Skills')
    Projects = request.args.get('Projects')
    Internships = request.args.get('Internships')
    Training = request.args.get('Training')
    Backlog = request.args.get('Backlog')
    arr = np.array([Coding_Skills,Aptitude_Skills,Technical_Skills,Communication_Skills,Core_Knowledge,Presentation_Skills,Academic_Performance,Puzzle_Solving_skills,English_Proficiency,Programming_Skills,Management_Skills,Projects,Internships,Training,Backlog])
    brr = np.asarray(arr)
    output = model.predict([brr])
    res = output[0] / 100
    if res > 0.7:
        res = str(round(res*100))
        val_str = ("All the very best, you are doing well!! Your placement chances are "+ res + " %")
        
    elif res > 0.4:
        res = str(round(res*100))
        val_str = ("Well Your placement chances will be " + res + " %,You need to prepare well!!")
        
    else:
        res = str(round(res*100))
        val_str = ("Well Your placement chances will be " + res +" %, You need to prepare well!!")
        
    return render_template('out.html', output=val_str)
if __name__ == "__main__":
    app.run(debug=True,port=9000)