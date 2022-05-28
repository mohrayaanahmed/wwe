import random as rd
Name = ['John Cena','Finn Balor','Andrade','Mustafa Ali','Baron Corbin','Sasha Banks',
        'Seth Rollins', 'Dean Ambrose','Drew Mcintyre','Daniel Bryan','Brock Lesnar',
        'Becky Lynch','Charlotte Flair','Velveteen Dream','Ricochet','Aleister Black',
        'Johnny Gargano','Tommaso Ciampa','Adam Cole','Lashley','Bayley','Braun Strowman',
        'AJ Styles','Randy Orton','Samoa Joe','The Miz','Cesaro','Xavier Woods','Elias',
        'Alexa Bliss','Dolph Ziggler','Ronda Rousey','Roderick Strong','Shinsuke Nakamura',
        'Bobby Roode','Dakota Kai','Asuka','Tyler Bate','William Regal','Fandango']
Popularity = [95,90,84,81,80,87,92,89,89,95,95,90,88,85,85,86,86,86,85,85,85,84,93,91,88,
              87,87,83,84,85,86,89,86,88,83,82,87,81,77,79]
Rank = [11,2,29,36,35,9,5,25,6,1,3,12,15,8,21,16,13,16,18,34,30,28,4,20,7,32,
        22,37,27,24,10,14,23,17,33,26,21,22,38,39]
Weight = [228,172,190,165,258,106,196,204,240,190,260,122,130,206,180,196,180,182,191,
          246,108,385,198,226,256,200,210,186,196,92,198,122,182,208,213,110,124,158,220,222]
Height = [185,180,175,178,203,165,185,188,196,178,191,168,178,188,175,180,178,180,183,
          191,168,203,180,196,188,188,196,180,183,155,183,170,178,188,185,168,160,170,190,193]

import pandas as pd

wwe = pd.DataFrame({'Name': Name})
wwe['Popularity'] = Popularity
wwe['Rank'] = Rank
wwe['Height'] = Height
wwe['Weight'] = Weight


play = 0
c = 0
s = 0


while(len(wwe) > 1):
    x = rd.choice(wwe.Name)
    y = rd.choice(wwe.Name)
    print("Player 1 picked up " +x)
    print("Player 2 picked up " +y)
    n = input("Choose either Popularity, Height, Weight or Rank")
    i = 0
    for a in wwe.Name:
        if (a == x):
            break
        i = i + 1
    j = 0
    for b in wwe.Name:
        if (b == y):
            break
        j = j + 1
    if(n == "Popularity" or n == " Popularity" or n == "popularity" or n == " popularity" or n == "p" or n == "P"):
        print("Popularity of " +wwe.Name[i]+ " is: " +str(wwe.Popularity[i]))
        print("Popularity of " +wwe.Name[j]+ " is: " +str(wwe.Popularity[j]))
        if(wwe.Popularity[i] > wwe.Popularity[j]):
            print(wwe.Name[i]+ " wins!")
            s = s + 1
        elif(wwe.Popularity[j] > wwe.Popularity[i]):
            print(wwe.Name[j]+ " wins!")
            c = c + 1
        else:
            print("DRAWWWW!!!")
    elif(n == "Rank" or n == " Rank" or n == "rank" or n == " rank" or n == "r" or n == "R"):
        print("Rank of " +wwe.Name[i]+ " is: " +str(wwe.Rank[i]))
        print("Rank of " +wwe.Name[j]+ " is: " +str(wwe.Rank[j]))
        if(wwe.Rank[i] > wwe.Rank[j]):
            print(wwe.Name[j]+ " wins!")
            c = c + 1
        elif(wwe.Rank[j] > wwe.Rank[i]):
            print(wwe.Name[i]+ " wins!")
            s = s + 1
        else:
            print("DRAWWWW!!!")
    elif(n == "Weight" or n == " Weight" or n == "weight" or n == " weight" or n == "w" or n == "W"):
        print("Weight of " +wwe.Name[i]+ " is: " +str(wwe.Weight[i]))
        print("Weight of " +wwe.Name[j]+ " is: " +str(wwe.Weight[j]))
        if(wwe.Weight[i] > wwe.Weight[j]):
            print(wwe.Name[i]+ " wins!")
            s = s + 1
        elif(wwe.Weight[j] > wwe.Weight[i]):
            print(wwe.Name[j]+ " wins!")
            c = c + 1
        else:
            print("DRAWWWW!!!")
    elif(n == "Height" or n == " Height" or n == "height" or n == " height" or n == "h" or n == "H"):
        print("Height of " +wwe.Name[i]+ " is: " +str(wwe.Height[i]))
        print("Height of " +wwe.Name[j]+ " is: " +str(wwe.Height[j]))
        if(wwe.Height[i] > wwe.Height[j]):
            print(wwe.Name[i]+ " wins!")
            s = s + 1
        elif(wwe.Height[j] > wwe.Height[i]):
            print(wwe.Name[j]+ " wins!")
            c = c + 1
        else:
            print("DRAWWWW!!!")
    else:
        print("No such category.")
    wwe = wwe.drop(i)
    if i != j:
        wwe = wwe.drop(j)
    wwe = wwe.reset_index(drop = True)
    input("\n")

if(s > c):
    print("Player 1 wins by " +str(s)+ " to " +str(c)+ " points.")
elif(c > s):
    print("Player 2 wins by " +str(c)+ " to " +str(s)+ " points.")
else:
    print("It's a Draw! Both players scored " +str(s)+ " points.")    
