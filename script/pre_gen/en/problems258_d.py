#Problem Statement
#We have a video game consisting of N stages. The i-th stage (1 ≦ i ≦ N) is composed of a movie lasting A_i minutes and gameplay lasting B_i minutes. 
#To clear the i-th stage for the first time, one must watch the movie and do the gameplay for that stage. For the second and subsequent times, one may skip the movie and do just the gameplay.
#In the beginning, only the 1-st stage is unlocked, and clearing the i-th stage (1 ≦ i ≦ N - 1) unlocks the (i+1)-th stage. 
#Find the shortest time needed to clear a stage X times in total. Here, if the same stage is cleared multiple times, all of them count.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ 10^9  (1 ≦ i ≦ N)
#1 ≦ X ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N X
#A_1 B_1
#.
#.
#.
#A_N B_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3 4
#3 4
#2 3
#4 2
#
#Sample Output 1
#18
#Here is one way to clear a stage 4 times in 18 minutes:
#Clear Stage 1. It takes A_1 + B_1 = 7 minutes.
#Clear Stage 2. It takes A_2 + B_2 = 5 minutes.
#Clear Stage 2 again. It takes B_2= 3 minutes.
#Clear Stage 2 again. It takes B_2= 3 minutes.
#It is impossible to clear a stage 4 times within 17 minutes.
#
#Sample Input 2
#10 1000000000
#3 3
#1 6
#4 7
#1 8
#5 7
#9 9
#2 4
#6 4
#5 1
#3 1
#
#Sample Output 2
#1000000076

def 