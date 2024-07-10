import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import output


#import results from 'output.py'
ext = (output.results[0]['ext'])
agr = (output.results[1]['agr'])
con = (output.results[2]['con'])
neu = (output.results[3]['neu'])
ope = (output.results[4]['ope'])
#uncomment below to test that file is importing correctly - should work as integers
print(ext,agr,con,neu,ope)


def main():
    N = 5
    user = (ext, agr, con, neu, ope) #LAN length of outage (mins)
    mean = (.548, .703, 0.67, .462, .631) #WAN length of outage (min)
    width = .35
    inu = np.arange(N)    # the x locations for the groups
    inm = [x + width for x in inu]
  
  

    # describe where to display p1
    plt.figure().set_figwidth(10)
    p1 = plt.bar(inm, mean, width, label="Study")
    p2 = plt.bar(inu, user, width, label="You")
    # stack p2 on top of p1

    #plt.figure(figsize=(7,4))

    # Describe the table metadata
    plt.ylabel("Trait Score")
    plt.title("Comparison to study averages")
    plt.xticks(inu+width, ("Extroversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"))
    plt.yticks(np.arange(0, 1.1, .1)) #.1 = first tick, 1= whole scale
    plt.legend((p1[0], p2[0]), ("Study", "You"))

    plt.savefig("/home/jesh/TLG python/mycode/project/ffm.pdf")
    

if __name__ == "__main__":
    main()
