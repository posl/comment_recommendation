#Problem Statement
#Given is an integer sequence A: A_1, A_2, A_3, ..., A_N.
#Let the GCD-ness of a positive integer k be the number of elements among A_1, A_2, A_3, ..., A_N that are divisible by k.
#Among the integers greater than or equal to 2, find the integer with the greatest GCD-ness. If there are multiple such integers, you may print any of them.  
#
#Constraints
#1 ≦ N ≦ 100
#2 ≦ A_i ≦ 1000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 A_3 ... A_N
#
#Output
#Print an integer with the greatest GCD-ness among the integers greater than or equal to 2. If there are multiple such integers, any of them will be accepted.
#
#Sample Input 1
#3
#3 12 7
#
#Sample Output 1
#3
#Among 3, 12, and 7, two of them - 3 and 12 - are divisible by 3, so the GCD-ness of 3 is 2.
#No integer greater than or equal to 2 has greater GCD-ness, so 3 is a correct answer.  
#
#Sample Input 2
#5
#8 9 18 90 72
#
#Sample Output 2
#9
#In this case, the GCD-ness of 9 is 4.
#2 and 3 also have the GCD-ness of 4, so you may also print 2 or 3.  
#
#Sample Input 3
#5
#1000 1000 1000 1000 1000
#
#Sample Output 3
#1000

def 