#Problem Statement
#There are N people, each of whom is either a child or an adult.  The i-th person has a weight of W_i.
#Whether each person is a child or an adult is specified by a string S of length N consisting of 0 and 1.
#If the i-th character of S is 0, then the i-th person is a child; if it is 1, then the i-th person is an adult.  
#When Takahashi the robot is given a real number X,
#Takahashi judges a person with a weight less than X to be a child and a person with a weight more than or equal to X to be an adult.
#For a real value X, let f(X) be the number of people whom Takahashi correctly judges whether they are children or adults.
#Find the maximum value of f(X) for all real values of X.
#
#Constraints
#1≦ N≦ 2× 10^5
#S is a string of length N consisting of 0 and 1.
#1≦ W_i≦ 10^9
#N and W_i are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S
#W_1 W_2 ... W_N
#
#Output
#Print the maximum value of f(X) as an integer in a single line.
#
#Sample Input 1
#5
#10101
#60 45 30 40 80
#
#Sample Output 1
#4
#When Takahashi is given X=50, it judges the 2-nd, 3-rd, and 4-th people to be children and the 1-st and 5-th to be adults.
#In reality, the 2-nd and 4-th are children, and the 1-st, 3-rd, and 5-th are adults, so the 1-st, 2-nd, 4-th, and 5-th people are correctly judged.
#Thus, f(50)=4.
#This is the maximum since there is no X that judges correctly for all 5 people.  Thus, 4 should be printed.
#
#Sample Input 2
#3
#000
#1 2 3
#
#Sample Output 2
#3
#For example, X=10 achieves the maximum value f(10)=3.
#Note that the people may be all children or all adults.
#
#Sample Input 3
#5
#10101
#60 50 50 50 60
#
#Sample Output 3
#4
#For example, X=55 achieves the maximum value f(55)=4.
#Note that there may be multiple people with the same weight.

def 