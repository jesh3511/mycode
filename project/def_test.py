E = 20
Ex = E/40
Em = .548
Es= 0.15

#Z score 
#   (value - mean) / std dev
def zscore(val, mean, std): 
    z = (((val-mean))/std)
    return z

#Percentile value 
#   mean + (z score * std dev)
def perc(mean, zscore, std):  
    p = (mean+(zscore*std))
    return p

Ez = zscore(Ex, Em, Es)
print(Ez)

Ep = (perc(Em, Ez, Es))*100
print(Ep)