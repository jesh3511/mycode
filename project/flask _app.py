import os
import json
from flask import Flask, render_template, request 
import ffm_func as ff
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



E=0
A=0
C=0
N=0
O=0


app = Flask(__name__)

try:
    os.chdir("/home/jesh/TLG python/mycode/project")

    #input_file = "dict.json"
    with open("dict.json", "r") as dict:
        question_list = json.load(dict)

except FileNotFoundError:
    print(f"Error: File '{dict.json}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

finally:
    val=[]
    for item in question_list:
        for value in item.values():
            val.append(value)



@app.route('/') 
@app.route('/quiz')
def quiz():
    return render_template("quiz.html", question_list = val, len = len(question_list)) 
    


@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    answers = {}
    for i, question in enumerate(question_list):
        key = f"answer{i+1}"
        question_text = question.get('question_text', f"{i+1}")
        answer_value = request.form.get(key)
        try:
            answers[question_text] = int(answer_value)
        except (ValueError, TypeError):
            answers[question_text] = "Conversion Failed" 
    print("Answers received:")
    with open('responses.json', 'w') as json_file:
        json.dump(answers, json_file)
    print(answers)

    a1 = answers['1']    
    a2 = answers['2']
    a3 = answers['3']
    a4 = answers['4']
    a5 = answers['5']
    a6 = answers['6']
    a7 = answers['7']
    a8 = answers['8']
    a9 = answers['9']
    a10=answers['10']
    a11=answers['11']
    a12=answers['12']
    a13=answers['13']
    a14=answers['14']
    a15=answers['15']
    a16=answers['16']
    a17=answers['17']
    a18=answers['18']
    a19=answers['19']
    a19=answers['19']
    a20=answers['20']
    a21=answers['21']
    a22=answers['22']
    a23=answers['23']
    a24=answers['24']
    a25=answers['25']
    a26=answers['26']
    a27=answers['27']
    a28=answers['28']
    a29=answers['29']
    a30=answers['30']
    a31=answers['31']
    a32=answers['32']
    a33=answers['33']
    a34=answers['34']
    a35=answers['35']
    a36=answers['36']
    a37=answers['37']
    a38=answers['38']
    a39=answers['39']
    a40=answers['40']
    a41=answers['41']
    a42=answers['42']
    a43=answers['43']
    a44=answers['44']
    a45=answers['45']
    a46=answers['46']
    a47=answers['47']
    a48=answers['48']
    a49=answers['49']
    a50=answers['50']

    global E
    E=(20+a1-a6+a11-a16+a21-a26+a31-a36+a41-a46)
    global A
    A=(14-a2+a7-a12+a17-a22+a27-a32+a37+a42+a47)
    global C
    C=(14+a3-a8+a13-a18+a23-a28+a33-a38+a43+a48)
    global N
    N=(38-a4+a9-a14+a19-a24-a29-a34-a39-a44-a49)
    global O
    O=(8+a5-a10+a15-a20+a25-a30+a35+a40+a45+a50)
    E, A, C, N, O
    return render_template("submit.html")
    


#class ma():


Ex = E/40
Em = .548
Es = 0.15
Ez = ff.zscore(Ex, Em, Es)
Ep = ff.perc(Em, Ez, Es)
Ax = A/40
Am = .703
As = .115
Az = ff.zscore(Ax, Am, As)
Ap = ff.perc(Am, Az, As)
Cx = C/40
Cm = 0.67
Cs = .159
Cz = ff.zscore(Cx, Cm, Cs)
Cp = ff.perc(Cm, Cz, Cs)
Nx = N/40
Nm = .462
Ns = .177
Nz = ff.zscore(Nx, Nm, Ns)
Np = ff.perc(Nm, Nz, Ns)
Ox = O/40
Om = .631
Os = .122
Oz = ff.zscore(Ox, Om, Os)
Op = ff.perc(Om, Oz, Os)


'''print("Ex test outside function:")
print(ma.Ex)'''
        
@app.route('/compare_data', methods=['POST'])
def compare_data():
    


    user = (Ex, Ax, Cx, Nx, Ox) 
    mean = (.548, .703, 0.67, .462, .631) 
    width = .35
    inu = np.arange(5)    
    inm = [x + width for x in inu]
  
    # describe where to display p1
    plt.figure().set_figwidth(10)
    p1 = plt.bar(inm, mean, width, label="Study")
    p2 = plt.bar(inu, user, width, label="You")

    # Describe the table metadata
    plt.ylabel("Trait Score")
    plt.title("Comparison to study averages")
    plt.xticks(inu+width, ("Extroversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"))
    plt.yticks(np.arange(0, 1.1, .1)) #.1 = first tick, 1= whole scale
    plt.legend((p1[0], p2[0]), ("Study", "You"))

    plt.savefig("/home/jesh/TLG python/mycode/project/static/ffm.png")
    return render_template("compare.html", E=Ep, A=Ap, C=Cp, N=Np, O=Op)





if __name__ == "__main__":
    app.run(use_reloader = True, debug = True) 
    


