import random2 as rand
import numpy as np

# Calculates Ratio
def CalculateRatioRandomized(DNA,Profile,k):
    Motifs = [] #Stores new Motifs

    AllRatio =[]

    for i in DNA:
       Ratio = []

       for j in range(len(i)-k+1):
            motif=i[j:j+k] #gets k-long substring starting from 0

            r = 1 #Sets initial ratio to zero
            #Calculates the ratio according to the profile matrix
            for n in range(k):
                if (motif[n] == 'A'):
                    r =Profile[n][0] * r
                elif (motif[n] == 'C'):
                    r =Profile[n][1] * r
                elif (motif[n] == 'G'):
                    r =Profile[n][2] * r
                elif (motif[n] == 'T'):
                    r =Profile[n][3] * r
            Ratio.append(r)
       index=Ratio.index((max(Ratio))) #finds the index of max ratio
       Motifs.append(i[index:index+k]) #adds the substring which has max ratio to motifs array
       AllRatio.append(Ratio)

    return Motifs
#calcutes the profile matrix
def CalculateProfileRandomized(Motifs,k):

    Profile = [] #Stores the profile matrix

    for i in range(0,k):
        countA = 0  # Stores each column's number of A's value
        countC = 0  # Stores each column's number of C's value
        countG = 0  # Stores each column's number of G's value
        countT = 0  # Stores each column's number of T's value
        num = []    #Stores the lines in motifs
        ProfileCount = []
        for line in Motifs:
            num.append(line[i])
        #Store the count values
        countA=num.count('A')
        countC = num.count('C')
        countG =num.count('G')
        countT = num.count('T')
        countTotal = countA + countT + countC + countG
        #calculates the ratio and stores them in the ProfileCount array
        ProfileCount.append(countA/countTotal)
        ProfileCount.append(countC / countTotal)
        ProfileCount.append(countG / countTotal)
        ProfileCount.append(countT / countTotal)
        Profile.append(ProfileCount)
    return Profile

# Calculates the score
def ScoreRandomized(Consensus,Score,Motifs,k,count):
    scoreTotal=0 #Stores the final score
    consensusString="" #Stores the consensus string
    tempArr =[] #Stores the max nucleotide names
    Report = [] #Stores the consensus string and the score for each iteration


    for i in range(0,k ):
        score = 0 #stores each column's score value
        countA = 0 #Stores each column's number of A's value
        countC = 0 #Stores each column's number of C's value
        countG = 0 #Stores each column's number of G's value
        countT = 0 #Stores each column's number of T's value

        Count = [] #Stores the count values

        for j in range(len(Motifs)): #Calculates the number of A's, T's, G's and C's value in a column
            if(Motifs[j][i] == 'A'):
                countA+=1
            if (Motifs[j][i] == 'T'):
                countT += 1
            if (Motifs[j][i] == 'G'):
                countG += 1
            if (Motifs[j][i] == 'C'):
                countC += 1
        #Adds the count values to count array to find max without iteration
        Count.append(countA)
        Count.append(countC)
        Count.append(countG)
        Count.append(countT)

        maxValue = max(Count) #Finds the max value

        #Adds nucleotide names to temp array to choose it randomly if there is an equality
        if(maxValue== countA):
            tempArr.append('A')
        if (maxValue == countT):
            tempArr.append('T')
        if (maxValue == countG):
            tempArr.append('G')
        if (maxValue == countC):
            tempArr.append('C')

        RandomNumber = rand.randint(0,len(tempArr)-1) #generates a number between 0 and length of the temp array -1
        consensusString = consensusString + tempArr[RandomNumber] #adds the nucleotide chosen to the consensus string
        countTotal = countA + countT + countC + countG
        score = (countTotal-maxValue)
        scoreTotal= score + scoreTotal
        tempArr.clear()
        temp=''
        Count.clear()
    Consensus.append(consensusString)
    Score.append(scoreTotal)
    count = count + 1



    return Consensus,Score, scoreTotal,count

def RandomlySelectMotifsRandomized(dna,k):
    #Motifs array store motif strings in an array
    Motifs=[]
    #generate a random number for every line and create a substring that will be our motif for each line and store the motif string
    for i in dna:
        RandomNumber = rand.randint(0, 500 - k)
        Motifs.append(i[RandomNumber:RandomNumber+k])
    return Motifs

#Reads the input file received from the user and puts them in a list
def CreateDNARandomized(fileName):
     file = open(fileName, 'r')
     DNA = [line.strip() for line in file]

     return DNA


