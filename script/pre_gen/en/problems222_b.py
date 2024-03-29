#Problem Statement
#N students took an exam. The students are labeled as Student 1, Student 2, ..., Student N, and Student i scored a_i points.
#A student who scored less than P points are considered to have failed the exam and cannot earn the credit. Find the number of students who failed the exam.
#
#Constraints
#1 ≦ N ≦ 10^5
#1 ≦ P ≦ 100
#0 ≦ a_i ≦ 100 (1 ≦ i ≦ N)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N P
#a_1 a_2 ... a_N
#
#Output
#Print the number of students who failed the exam.
#
#Sample Input 1
#4 50
#80 60 40 0
#
#Sample Output 1
#2
#Students 1 and 2, who scored 80 and 60 points, respectively, succeeded in scoring at least 50 points to earn the credit.
#On the other hand, Students 3 and 4, who scored 40 and 0 points, respectively, fell below 50 points and failed the exam. Thus, the answer is 2.
#
#Sample Input 2
#3 90
#89 89 89
#
#Sample Output 2
#3
#
#Sample Input 3
#2 22
#6 37
#
#Sample Output 3
#1

def 