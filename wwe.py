import random as rd
Name = ['John Cena','Finn Balor','Andrade','Mustafa Ali','Baron Corbin','Sasha Banks',
        'Seth Rollins', 'Dean Ambrose','Drew Mcintyre','Daniel Bryan','Brock Lesnar',
        'Becky Lynch','Charlotte Flair','Velveteen Dream','Ricochet','Aleister Black',
        'Johnny Gargano','Tommaso Ciampa','Adam Cole','Lashley','Bayley','Braun Strowman',
        'AJ Styles','Randy Orton','Samoa Joe','The Miz','Cesaro','Xavier Woods','Elias',
        'Alexa Bliss','Dolph Ziggler','Ronda Rousey','Roderick Strong','Shinsuke Nakamura',
        'Bobby Roode','Dakota Kai','Asuka','Tyler Bate']
Popularity = [95,90,84,81,80,87,92,89,89,95,95,90,88,85,85,86,86,86,85,85,85,84,93,91,88,
              87,87,83,84,85,86,89,86,88,83,82,87,81]
Rank = [11,2,29,36,35,9,5,25,6,1,3,12,15,8,21,16,13,16,18,34,29,28,4,20,7,32,
        22,37,27,24,10,14,23,17,33,26,21,22]
Weight = [228,172,190,165,258,106,196,204,240,190,260,122,130,206,180,196,180,182,191,
          246,108,385,198,226,256,200,210,186,196,92,198,122,182,208,213,110,124,158]
play=0
c=0
s=0

while(play<10):
    x = rd.choice(Name)
    y = rd.choice(Name)
    print("Player 1 picked up " +x)
    print("Player 2 picked up " +y)
    n = input("Choose either Popularity, Weight or Rank")
    i=0
    for a in Name:
        if (a==x):
            break
        i=i+1
    j=0
    for b in Name:
        if (b==y):
            break
        j=j+1
    if(n=="Popularity" or n==" Popularity" or n=="popularity" or n==" popularity"):
        print("Popularity of " +Name[i]+ " is: " +str(Popularity[i]))
        print("Popularity of " +Name[j]+ " is: " +str(Popularity[j]))
        if(Popularity[i] > Popularity[j]):
            print(Name[i]+ " wins!")
            s=s+1
        elif(Popularity[j] > Popularity[i]):
            print(Name[j]+ " wins!")
            c=c+1
        else:
            print("DRAWWWW!!!")
    elif(n=="Rank" or n==" Rank" or n=="rank" or n==" rank"):
        print("Rank of " +Name[i]+ " is: " +str(Rank[i]))
        print("Rank of " +Name[j]+ " is: " +str(Rank[j]))
        if(Rank[i] > Rank[j]):
            print(Name[j]+ " wins!")
            c=c+1
        elif(Rank[j] > Rank[i]):
            print(Name[i]+ " wins!")
            s=s+1
        else:
            print("DRAWWWW!!!")
    elif(n=="Weight" or n==" Weight" or n=="weight" or n==" weight"):
        print("Weight of " +Name[i]+ " is: " +str(Weight[i]))
        print("Weight of " +Name[j]+ " is: " +str(Weight[j]))
        if(Weight[i] > Weight[j]):
            print(Name[i]+ " wins!")
            s=s+1
        elif(Weight[j] > Weight[i]):
            print(Name[j]+ " wins!")
            c=c+1
        else:
            print("DRAWWWW!!!")
    else:
        print("No such category.")
    play=play+1
    input("\n")
if(s>c):
    print("Player 1 wins by " +str(s)+ " to " +str(c)+ " points.")
elif(c>s):
    print("Player 2 wins by " +str(c)+ " to " +str(s)+ " points.")
else:
    print("It's a Draw! Both players scored " +str(s)+ " points.")
