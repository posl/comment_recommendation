#Problem Statement
#You have a sequence A composed of N positive integers: A_{1}, A_{2}, ..., A_{N}.
#You will now successively do the following Q operations:
#In the i-th operation, you replace every element whose value is B_{i} with C_{i}.
#For each i (1 ≦ i ≦ Q), find S_{i}: the sum of all elements in A just after the i-th operation.
#
#Constraints
#All values in input are integers.
# 1 ≦ N, Q, A_{i}, B_{i}, C_{i} ≦ 10^{5} 
# B_{i} ≠ C_{i} 
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_{1} A_{2} ... A_{N}
#Q
#B_{1} C_{1}
#B_{2} C_{2}
#.
#.
#.
#B_{Q} C_{Q}
#
#Output
#Print Q integers S_{i} to Standard Output
# in the following format:
#S_{1}
#S_{2}
#.
#.
#.
#S_{Q}
#Note that S_{i} may not fit into a 32-bit integer.
#
#Sample Input 1
#4
#1 2 3 4
#3
#1 2
#3 4
#2 4
#
#Sample Output 1
#11
#12
#16
#Initially, the sequence A is 1,2,3,4.
#After each operation, it becomes the following:
#2, 2, 3, 4
#2, 2, 4, 4
#4, 4, 4, 4
#
#Sample Input 2
#4
#1 1 1 1
#3
#1 2
#2 1
#3 5
#
#Sample Output 2
#8
#4
#4
#Note that the sequence A may not contain an element whose value is B_{i}.
#
#Sample Input 3
#2
#1 2
#3
#1 100
#2 100
#100 1000
#
#Sample Output 3
#102
#200
#2000

def 