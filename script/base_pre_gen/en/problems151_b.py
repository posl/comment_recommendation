#Problem Statement
#Takahashi is taking exams on N subjects. The score on each subject will be an integer between 0 and K (inclusive).
#He has already taken exams on N-1 subjects and scored A_i points on the i-th subject.
#His goal is to achieve the average score of M points or above on the N subjects.
#Print the minimum number of points Takahashi needs on the final subject to achieve his goal.
#If the goal is unachievable, print -1 instead.
#
#Constraints
#2 ≦ N ≦ 100
#1 ≦ K ≦ 100
#1 ≦ M ≦ K
#0 ≦ A_i ≦ K
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K M
#A_1 A_2 ... A_{N-1}
#
#Output
#Print the minimum number of points required on the final subject, or -1.
#
#Sample Input 1
#5 10 7
#8 10 3 6
#
#Sample Output 1
#8
#If he scores 8 points on the final subject, his average score will be (8+10+3+6+8)/5 = 7 points, which meets the goal.
#
#Sample Input 2
#4 100 60
#100 100 100
#
#Sample Output 2
#0
#Scoring 0 points on the final subject still meets the goal.
#
#Sample Input 3
#4 100 60
#0 0 0
#
#Sample Output 3
#-1
#He can no longer meet the goal.

def 