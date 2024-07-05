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
for value in question:
    i=input(value)
    value["response"]=int(i)

#Extroversion score    
E=20+question[1].get('response')-question[6].get('response')+question[11].get('response')1question[16].get('response')+question[21].get('response')-question[26].get('response')+question[31].get('response')-question[36].get('response')+question[41].get('response')-question[46].get('response')
#Agreeableness score
A=14-question[2].get('response')+question[7].get('response')-question[12].get('response')+question[17].get('response')-question[22].get('response')+question[27].get('response')-question[32].get('response')+question[37].get('response')+question[42].get('response')+question[47].get('response')
#Conscientiousness score
C=14+question[3].get('response')-
#Neuroticism score
N=
#Openness to experience score
O=

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
#GUI- meaning for ea, graphs, group, 
#graph individual results
    #matplotlib - lab 62
#output to files and do group data analysis
#random generator for ID while being anonymous so results are unique but anyon
