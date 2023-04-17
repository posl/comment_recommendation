#Problem Statement
#In Takahashi Kingdom, there is a east-west railroad and N cities along it, numbered 1, 2, 3, ..., N from west to east.
#A company called AtCoder Express possesses M trains, and the train i runs from City L_i to City R_i (it is possible that L_i = R_i).
#Takahashi the king is interested in the following Q matters:
#The number of the trains that runs strictly within the section from City p_i to City q_i, that is, the number of trains j such that p_i ≦ L_j and R_j ≦ q_i.
#Although he is genius, this is too much data to process by himself. Find the answer for each of these Q queries to help him.
#
#Constraints
#N is an integer between 1 and 500 (inclusive).
#M is an integer between 1 and 200  000 (inclusive).
#Q is an integer between 1 and 100  000 (inclusive).
#1 ≦ L_i ≦ R_i ≦ N (1 ≦ i ≦ M)
#1 ≦ p_i ≦ q_i ≦ N (1 ≦ i ≦ Q)
#
#Input
#Input is given from Standard Input in the following format:
#N M Q
#L_1 R_1
#L_2 R_2
#:
#L_M R_M
#p_1 q_1
#p_2 q_2
#:
#p_Q q_Q
#
#Output
#Print Q lines. The i-th line should contain the number of the trains that runs strictly within the section from City p_i to City q_i.
#
#Sample Input 1
#2 3 1
#1 1
#1 2
#2 2
#1 2
#
#Sample Output 1
#3
#As all the trains runs within the section from City 1 to City 2, the answer to the only query is 3.
#
#Sample Input 2
#10 3 2
#1 5
#2 8
#7 10
#1 7
#3 10
#
#Sample Output 2
#1
#1
#The first query is on the section from City 1 to 7. There is only one train that runs strictly within that section: Train 1.
#The second query is on the section from City 3 to 10. There is only one train that runs strictly within that section: Train 3.
#
#Sample Input 3
#10 10 10
#1 6
#2 9
#4 5
#4 7
#4 7
#5 8
#6 6
#6 7
#7 9
#10 10
#1 8
#1 9
#1 10
#2 8
#2 9
#2 10
#3 8
#3 9
#3 10
#1 10
#
#Sample Output 3
#7
#9
#10
#6
#8
#9
#6
#7
#8
#10

def 