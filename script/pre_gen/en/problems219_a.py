#Problem Statement
#In the Kingdom of AtCoder, there is a standardized test of competitive programming proficiency.
#An examinee will get a score out of 100 and obtain a rank according to the score, as follows:
#Novice, for a score not less than 0 but less than 40;
#Intermediate, for a score not less than 40 but less than 70;
#Advanced, for a score not less than 70 but less than 90;
#Expert, for a score not less than 90.
#Takahashi took this test and got X points.
#Find the minimum number of extra points needed to go up one rank higher. If, however, his rank was Expert, print expert, as there is no higher rank than that. 
#
#Constraints
#0 ≦ X ≦ 100
#X is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#X
#
#Output
#Print the answer.
#
#Sample Input 1
#56
#
#Sample Output 1
#14
#He got 56 points and was certified as Intermediate. In order to reach the next rank of Advanced, he needs at least 14 more points.
#
#Sample Input 2
#32
#
#Sample Output 2
#8
#
#Sample Input 3
#0
#
#Sample Output 3
#40
#
#Sample Input 4
#100
#
#Sample Output 4
#expert
#He got full points and was certified as Expert. There is no rank higher than that, so print expert.

def 