#Problem Statement
#Takahashi is a teacher responsible for a class of N students.
#The students are given distinct student numbers from 1 to N.
#Today, all the students entered the classroom at different times.
#According to Takahashi's record, there were A_i students in the classroom when student number i entered the classroom (including student number i).
#From these records, reconstruct the order in which the students entered the classroom.
#
#Constraints
# 1 ≦ N ≦ 10^5 
# 1 ≦ A_i ≦ N 
# A_i ≠ A_j  (i ≠ j)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the student numbers of the students in the order the students entered the classroom.
#
#Sample Input 1
#3
#2 3 1
#
#Sample Output 1
#3 1 2
#First, student number 3 entered the classroom.
#Then, student number 1 entered the classroom.
#Finally, student number 2 entered the classroom.
#
#Sample Input 2
#5
#1 2 3 4 5
#
#Sample Output 2
#1 2 3 4 5
#
#Sample Input 3
#8
#8 2 7 3 4 5 6 1
#
#Sample Output 3
#8 2 4 5 6 7 3 1

def 