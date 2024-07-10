#E = 34
#Ex = E/40
#Em = .548
#Es= 0.15

#Z score 
#   (value - mean) / std dev
def zscore(val, mean, std): 
    z = (((val-mean))/std)
    return z

#Percentile value 
#   mean + (z score * std dev)
def perc(mean, zscore, std):  
    p = (mean+(zscore*std))*100
    return p

#Add the correct suffix in the result for percentile scores
    #ex: 1st, 2nd, 3rd, 4th
def add_suffix(res):
    suffix = ""
    if res % 10 == 1 and res != 11:
        suffix = "st"
    elif res % 10 == 2 and res != 12:
        suffix = "nd"
    elif res % 10 == 3 and res != 13:
        suffix = "rd"
    else:
        suffix = "th"
    #res2 = str('%.3g' % res)
    #return res2 + suffix
    return str(('%.4f' % res).rstrip('0').rstrip('.')) +suffix

    
#Ez = zscore(Ex, Em, Es)
#Ep = perc(Em, Ez, Es)
#print(add_suffix(Ep))

#Ez = zscore(Ex, Em, Es)
#print(Ez)

#Ep = (perc(Em, Ez, Es))*100
#print(Ep)