import numpy as np
import random2 as rand

def ScoreGibbs(Motifs,k,count,Consensus,Score):
    scoreTotal=0
    consensusString=""
    tempArr =[]
    temp =""


    for i in range(0,k ):
        score = 0
        countA = 0
        countC = 0
        countG = 0
        countT = 0

        Count = []


        for j in range(len(Motifs)):
            if(Motifs[j][i] == 'A'):
                countA+=1
            if (Motifs[j][i] == 'T'):
                countT += 1
            if (Motifs[j][i] == 'G'):
                countG += 1
            if (Motifs[j][i] == 'C'):
                countC += 1

        Count.append(countA)
        Count.append(countC)
        Count.append(countG)
        Count.append(countT)

        maxValue = max(Count)

        if(countA>countT and countA>countC and countA>countG ):
            temp='A'
        if (countT > countA and countT > countC and countT > countG ):
             temp = 'T'
        if (countC > countT and countC> countA and countC > countG):
            temp = 'C'
        if (countG > countT  and countG > countC and countG > countA):
            temp = 'G'
        if(temp == ''):
            if(maxValue== countA):
                tempArr.append('A')
            if (maxValue == countT):
                tempArr.append('T')
            if (maxValue == countG):
                tempArr.append('G')
            if (maxValue == countC):
                tempArr.append('C')

            RandomNumber = rand.randint(0,len(tempArr)-1)
            temp = tempArr[RandomNumber]
        consensusString = consensusString + temp


        countTotal = countA + countT + countC + countG
        score = (countTotal-maxValue)
        scoreTotal=score+scoreTotal
        tempArr.clear()
        temp=''
        Count.clear()
    Consensus.append(consensusString)
    Score.append(scoreTotal)
    count = count + 1

    return Consensus,Score, scoreTotal,count

#Generates substing from the deleted line of dna and randomly selects the new motif
def FindOptimalMotif(deletedDna,Profile,k,Motif):
    Ratio = []
    count=0
    for i in range(len(deletedDna)-k+1):

       motif = deletedDna[i:i + k] #Generates k-long substing from the deleted line of dna starting from 0
       r = 1
       for n in range(k):

           if (motif[n] == 'A'):
               r = Profile[n][0] * r
           elif (motif[n] == 'C'):
               r = Profile[n][1] * r
           elif (motif[n] == 'G'):
               r = Profile[n][2] * r
           elif (motif[n] == 'T'):
               r = Profile[n][3] * r

       Ratio.append(r)


    index = Ratio.index(max(Ratio))
    motif = deletedDna[index:index+k]

    return motif

#Gets deleted dna string and add the new motif to the index
def ReplaceNewMotif(Dna,deletedDna,Motifs,index,motif):
    Dna.insert(index,deletedDna)
    Motifs.insert(index,motif) #Gets motifs string and add the new motif to the index
    return Dna,Motifs

def CalculateProfileGibbs(Motifs,k):

    Profile = [] #Stores the profile matrix

    for i in range(0,k):
        countA = 0  # Stores each column's number of A's value
        countC = 0  # Stores each column's number of C's value
        countG = 0  # Stores each column's number of G's value
        countT = 0  # Stores each column's number of T's value
        num = []     #Stores the lines in motifs
        ProfileCount = []
        for line in Motifs:
            num.append(line[i])
        # Store the count values
        countA=num.count('A')+1
        countC = num.count('C')+1
        countG =num.count('G')+1
        countT = num.count('T')+1
        countTotal = countA + countT + countC + countG
        # calculates the ratio and stores them in the ProfileCount array
        ProfileCount.append(countA/countTotal)
        ProfileCount.append(countC / countTotal)
        ProfileCount.append(countG / countTotal)
        ProfileCount.append(countT / countTotal)
        Profile.append(ProfileCount)

    return Profile

def DeleteDna(Dna,Motifs):

    RandomNumber = rand.randint(0,len(Dna)-1)
    deletedDna = Dna[RandomNumber]
    Dna.pop(RandomNumber)
    Motifs.pop(RandomNumber)
    return Dna, RandomNumber, deletedDna
#Reads the input file received from the user and puts them in a list
def CreateDNAGibbs(fileName):
    file = open(fileName, 'r')
    DNA = [line.strip() for line in file]
    return DNA


def RandomlySelectMotifGibbs(dna,k):
    #Motifs array store motif strings in an array
    Motifs=[]
    #generate a random number for every line and create a substring that will be our motif for each line and store the motif string
    for i in dna:
        RandomNumber = rand.randint(0, 500 - k)
        Motifs.append(i[RandomNumber:RandomNumber+k])
    return Motifs