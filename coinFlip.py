import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    listofcoins = []
    #listofTails = ['T']
    listofTails = ['T','T','T','T','T','T']
    listofHeads = ['H','H','H','H','H','H']
    
    for i in range(100):  
        if random.randint(0,1) == 1:
            listofcoins.append('T')
        else :
            listofcoins.append('H')

    for j in range(len(listofcoins)-6):
        tempList = []
        for k in range (0,6):
            tempList.append(listofcoins[j+k])
        if tempList == listofHeads :
            numberOfStreaks += 1
        elif tempList == listofTails :
            numberOfStreaks += 1 


print('Chance of streak : %s%%' %(numberOfStreaks/(100*10000)))
       
    