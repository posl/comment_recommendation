#Problem Statement
#Takahashi has decided to hold some number of programming contests.
#Holding one contest requires one 100-point problem, one 200-point problem, one 300-point problem, and one 400-point problem.
#When he has A_1, A_2, A_3, and A_4 drafts of 100-, 200-, 300-, and 400-point problems, respectively, at most how many contests can he hold?
#The same draft can be used only once.
#
#Constraints
#1 ≦ A_i ≦ 100 (1 ≦ i ≦ 4)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A_1 A_2 A_3 A_4
#
#Output
#Print an integer representing the maximum number of contests that can be held.  
#
#Sample Input 1
#5 3 7 11
#
#Sample Output 1
#3
#By using three drafts for each slot, he can hold three contests.
#He has just three drafts for 200-point problems, so he cannot hold four.
#
#Sample Input 2
#100 100 1 100
#
#Sample Output 2
#1
#A contest cannot be held even if there is just one missing slot.

def 