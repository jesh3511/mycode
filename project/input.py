#!/usr/bin/env python3
from ffm_func import zscore,perc,add_suffix


#question bank
question = [
    {"I...   ":"(Enter 1 to continue)"},
    {1:"Am the life of the party.",},
    {2:"Feel little concern for others."},
    {3:"Am always prepared."},
    {4:"Get stressed out easily."},
    {5:"Have a rich vocabulary."},
    {6:"Don't talk a lot."},
    {7:"Am interested in people."},
    {8:"Leave my belongings around."},
    {9:"Am relaxed most of the time."},
    {10:"Have difficulty understanding abstract ideas."},
    {11:"Feel comfortable around people."},
    {12:"Insult people."},
    {13:"Pay attention to details."},
    {14:"Worry about things."},
    {15:"Have a vivid imagination."},
    {16:"Keep in the background."},
    {17:"Sympathize with others' feelings."},
    {18:"Make a mess of things."},
    {19:"Seldom feel blue."},
    {20:"Am not interested in abstract ideas."},
    {21:"Start conversations."},
    {22:"Am not interested in other people's problems."},
    {23:"Get chores done right away."},
    {24:"Am easily disturbed."},
    {25:"Have excellent ideas."},
    {26:"Have little to say."},
    {27:"Have a soft heart."},
    {28:"Often forget to put things back in their proper place."},
    {29:"Get upset easily."},
    {30:"Do not have a good imagination."},
    {31:"Talk to a lot of different people at parties."},
    {32:"Am not really interested in others."},
    {33:"Like order."},
    {34:"Change my mood a lot."},
    {35:"Am quick to understand things."},
    {36:"Don't like to draw attention to myself."},
    {37:"Take time out for others."},
    {38:"Shirk my duties."},
    {39:"Have frequent mood swings."},
    {40:"Use difficult words."},
    {41:"Don't mind being the center of attention."},
    {42:"Feel others' emotions."},
    {43:"Follow a schedule."},
    {44:"Get irritated easily."},
    {45:"Spend time reflecting on things."},
    {46:"Am quiet around strangers."},
    {47:"Make people feel at ease."},
    {48:"Am exacting in my work."},
    {49:"Often feel blue."},
    {50:"Am full of ideas."},
]
#display the input prompt
print("For the following questions, answer on a scale from 1 to 5. \n1=Disagree\n2=Slightly Disagree\n3=Neutral\n4=Slightly agree\n5=Agree")

#display the question and register input
for value in question:
    k=list(value.keys())[0]
    i=input(f'{k}. {value.get(k)}')
    while int(i) <1 or int(i) > 5:
        i=input("\n====== Error:Please re-enter a number 1-5. ====== \n")
    value["response"]=i
    
#variables for each question
a1=int(question[1].get('response'))
a2=int(question[2].get('response'))
a3=int(question[3].get('response'))
a4=int(question[4].get('response'))
a5=int(question[5].get('response'))
a6=int(question[6].get('response'))
a7=int(question[7].get('response'))
a8=int(question[8].get('response'))
a9=int(question[9].get('response'))
a10=int(question[10].get('response'))
a11=int(question[11].get('response'))
a12=int(question[12].get('response'))
a13=int(question[13].get('response'))
a14=int(question[14].get('response'))
a15=int(question[15].get('response'))
a16=int(question[16].get('response'))
a17=int(question[17].get('response'))
a18=int(question[18].get('response'))
a19=int(question[19].get('response'))
a20=int(question[20].get('response'))
a21=int(question[21].get('response'))
a22=int(question[22].get('response'))
a23=int(question[23].get('response'))
a24=int(question[24].get('response'))
a25=int(question[25].get('response'))
a26=int(question[26].get('response'))
a27=int(question[27].get('response'))
a28=int(question[28].get('response'))
a29=int(question[29].get('response'))
a30=int(question[30].get('response'))
a31=int(question[31].get('response'))
a32=int(question[32].get('response'))
a33=int(question[33].get('response'))
a34=int(question[34].get('response'))
a35=int(question[35].get('response'))
a36=int(question[36].get('response'))
a37=int(question[37].get('response'))
a38=int(question[38].get('response'))
a39=int(question[39].get('response'))
a40=int(question[40].get('response'))
a41=int(question[41].get('response'))
a42=int(question[42].get('response'))
a43=int(question[43].get('response'))
a44=int(question[44].get('response'))
a45=int(question[45].get('response'))
a46=int(question[46].get('response'))
a47=int(question[47].get('response'))
a48=int(question[48].get('response'))
a49=int(question[49].get('response'))
a50=int(question[50].get('response'))

#Calculating Big Five scores
#Extroversion score (40 max 0 min)    
E=20+a1-a6+a11-a16+a21-a26+a31-a36+a41-a46
#Agreeableness score (40 max 0 min)
A=14-a2+a7-a12+a17-a22+a27-a32+a37+a42+a47
#Conscientiousness score (40 max 0 min)
C=14+a3-a8+a13-a18+a23-a28+a33-a38+a43+a48
#Neuroticism score (40 max 0 min)
N=38-a4+a9-a14+a19-a24-a29-a34-a39-a44-a49
#Openness to experience score (40 max 0 min)
O=8+a5-a10+a15-a20+a25-a30+a35+a40+a45+a50


#Print results to screen
print("")
print("Extroversion score = ", E)
print("Agreeableness score = ", A)
print("Conscientiousness score = ", C)
print("Neuroticism score = ", N)
print("Openness to experience score = ", O)
print("")


#Print only variables to file 'output' as a list of dictionaries
with open("output.py", "w") as outfile:
    print("#!/usr/bin/env python3\n\n", file=outfile)
    print("results = [", file=outfile)
    #can i turn all of this into a for loop??????
    print("{E : ", E/40, "},", sep="", file=outfile)
    print("{A : ", A/40, "},", sep="", file=outfile)
    print("{C : ", C/40, "},", sep="", file=outfile)
    print("{N : ", N/40, "},", sep="", file=outfile)
    print("{O : ", O/40, "},", sep="", file=outfile)
    print("]", file=outfile)


#calculate percentage
#Xx = calculated value out of a maximum score of 40
#Xm = mean score for trait
#Xs = std dev for trait
#Xz = z score = difference from mean / std dev
#Xp = percentile value = mean + (z score * std dev)


Ex = E/40
Em = .548
Es= 0.15
Ez = zscore(Ex, Em, Es)
Ep = perc(Em, Ez, Es)
Ax = A/40
Am = .703
As = .115
Az = zscore(Ax, Am, As)
Ap = perc(Am, Az, As)
Cx = C/40
Cm = 0.67
Cs = .159
Cz = zscore(Cx, Cm, Cs)
Cp = perc(Cm, Cz, Cs)
Nx = N/40
Nm = .462
Ns = .177
Nz = zscore(Nx, Nm, Ns)
Np = perc(Nm, Nz, Ns)
Ox = O/40
Om = .631
Os = .122
Oz = zscore(Ox, Om, Os)
Op = perc(Om, Oz, Os)
#Output percentiles as human readable



print(f"Your Extroversion score is in the {add_suffix(Ep)} percentile of the population.")
print(f"Your Agreeableness score is in the {add_suffix(Ap)} percentile of the population.")
print(f"Your Conscientiousness score is in the {add_suffix(Cp)} percentile of the population.")
print(f"Your Neuroticism score is in the {add_suffix(Np)} percentile of the population.")
print(f"Your Openness to experience score is in the {add_suffix(Op)} percentile of the population.")
print("")







#if name = main
#make error message repeat with additional invalid inputs
    #maybe put in seperate file and import
    #seperate code for input, results+graphs, export/import and netcode
        #sep dict
        #work on flask front end
    #library can be all code that does not need to run
        #ex: math for score calc and other methodology, dict
#if statements for scores to categorize and summarize
#while input DNE 1-5, repeat question
#GUI- meaning for ea, graphs, group, 
#graph individual results
    #matplotlib - lab 62
#output to files and do group data analysis
#random generator for ID while being anonymous so results are unique but anyon
#work with file objects