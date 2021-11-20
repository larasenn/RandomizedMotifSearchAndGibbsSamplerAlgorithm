import statistics
import time

from Gibbs import DeleteDna, FindOptimalMotif, ReplaceNewMotif, ScoreGibbs, CalculateProfileGibbs, \
    RandomlySelectMotifGibbs, CreateDNAGibbs
from RandomizedMotifSearch import CreateDNARandomized, RandomlySelectMotifsRandomized, \
    CalculateProfileRandomized, ScoreRandomized, CalculateRatioRandomized

if __name__ == '__main__':
    k = int(input("Enter k value (could be 9,10 or 11): "))
    fileName = input("Enter file name: ")
    Dna = CreateDNAGibbs(fileName)
    Motifs = RandomlySelectMotifGibbs(Dna, k)
    DNA = CreateDNARandomized(fileName)
    count = 1
    temp = 0
    iter = 1
    #Gibbs
    start_time = time.time()
    Consensus = []
    Score= []

    print("Gibbs Sampler with k = " + str(k))
    while(count < 50):

        Dna, index, deletedDna = DeleteDna(Dna,Motifs)
        Profile = CalculateProfileGibbs(Motifs, k)
        motif = FindOptimalMotif(deletedDna, Profile, k, Motifs)
        Dna, Motifs = ReplaceNewMotif(Dna, deletedDna, Motifs, index, motif)
        Consensus,Score, score ,iter= ScoreGibbs(Motifs, k,iter,Consensus,Score)

        if(temp == score):
            count += 1

        else:
            count = 1
        temp = score
    print("Motifs: " + str(Motifs))
    print("Best Score: " + str(min(Score)))
    print("Max Score: " +str(max(Score)) )
    print("Average Score: " + str(statistics.mean(Score)))
    print("Execution time: " + str(time.time() - start_time))
    print("Consensus String: " + str(Consensus))


    count = 1
    temp = 0
    iter = 1

    Motifs = RandomlySelectMotifsRandomized(DNA, k)
    Consensus = []
    Score = []
    print("Randomized Motif Search with k = " + str(k))
    #RandomizedMotifSearch
    while(count < 50):


        Profile = CalculateProfileRandomized(Motifs,k)
        Motifs = CalculateRatioRandomized(Dna,Profile,k)
        Consensus,Score, score ,iter= ScoreRandomized(Consensus,Score,Motifs, k,iter)

        if (temp == score):
            count += 1

        else:
            count = 1
        temp = score
    print("Motifs: " + str(Motifs))
    print("Best Score: " + str(min(Score)))
    print("Max Score: " + str(max(Score)))
    print("Average Score: " + str(statistics.mean(Score)))
    print("Execution time: " + str(time.time() - start_time))
    print("Consensus String: " + str(Consensus))
    


