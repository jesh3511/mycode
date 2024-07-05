#!/usr/bin/env python3
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
#print("\nI...\n")

#display the question and register input

while True:
    for value in question:
        i=input(value)
        value["response"]=int(i)
    if i >=1 and i <=5:
        break
    else:
        print("=====Error: answer must be entered as a number 1-5===== \n")

#variables for each question
a1=question[1].get('response')
a2=question[2].get('response')
a3=question[3].get('response')
a4=question[4].get('response')
a5=question[5].get('response')
a6=question[6].get('response')
a7=question[7].get('response')
a8=question[8].get('response')
a9=question[9].get('response')
a10=question[10].get('response')
a11=question[11].get('response')
a12=question[12].get('response')
a13=question[13].get('response')
a14=question[14].get('response')
a15=question[15].get('response')
a16=question[16].get('response')
a17=question[17].get('response')
a18=question[18].get('response')
a19=question[19].get('response')
a20=question[20].get('response')
a21=question[21].get('response')
a22=question[22].get('response')
a23=question[23].get('response')
a24=question[24].get('response')
a25=question[25].get('response')
a26=question[26].get('response')
a27=question[27].get('response')
a28=question[28].get('response')
a29=question[29].get('response')
a30=question[30].get('response')
a31=question[31].get('response')
a32=question[32].get('response')
a33=question[33].get('response')
a34=question[34].get('response')
a35=question[35].get('response')
a36=question[36].get('response')
a37=question[37].get('response')
a38=question[38].get('response')
a39=question[39].get('response')
a40=question[40].get('response')
a41=question[41].get('response')
a42=question[42].get('response')
a43=question[43].get('response')
a44=question[44].get('response')
a45=question[45].get('response')
a46=question[46].get('response')
a47=question[47].get('response')
a48=question[48].get('response')
a49=question[49].get('response')
a50=question[50].get('response')

#Calculating Big Five scores
#Extroversion score    
E=20+a1-a6+a11-a16+a21-a26+a31-a36+a41-a46
#Agreeableness score
A=14-a2+a7-a12+a17-a22+a27-a32+a37+a42+a47
#Conscientiousness score
C=14+a3-a8+a13-a18+a23-a28+a33-a38+a43+a48
#Neuroticism score
N=38-a4+a9-a14+a19-a24-a29-a34-a39-a44-a49
#Openness to experience score
O=8+a5-a10+a15-a20+a25-a30+a35+a40+a45+a50

#Print results

print("Extroversion score = ", E)
print("Agreeableness score = ", A)
print("Conscientiousness score = ", C)
print("Neuroticism score = ", N)
print("Openness to experience score = ", O)

#future plans:
#if name = main
#functions in alphabetical order
    #maybe put in seperate file and import
    #seperate code for input, results+graphs, export/import and netcode
    #library can be all code that does not need to run
        #ex: math for score calc and other methodology, dict
#if statements for scores to categorize and summarize
#while input DNE 1-5, repeat question
#GUI- meaning for ea, graphs, group, 
#graph individual results
    #matplotlib - lab 62
#output to files and do group data analysis
#random generator for ID while being anonymous so results are unique but anyon
