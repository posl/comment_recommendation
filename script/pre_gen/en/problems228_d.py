#Problem Statement
#There is a sequence A = (A_0, A_1, ..., A_{N - 1}) with N = 2^{20} terms. Initially, every term is -1.
#Process Q queries in order. The i-th query (1 ≦ i ≦ Q) is described by an integer t_i such that t_i = 1 or t_i = 2, and another integer x_i, as follows.
#If t_i = 1, do the following in order.
#Define an integer h as h = x_i.
#While A_{h mod N} ≠ -1, keep adding 1 to h. We can prove that this process ends after finite iterations under the Constraints of this problem.
#Replace the value of A_{h mod N} with x_i.
#If t_i = 2, print the value of A_{x_i mod N} at that time.
#Here, for integers a and b, a mod b denotes the remainder when a is divided by b.
#
#Constraints
#1 ≦ Q ≦ 2 × 10^5
#t_i in { 1, 2 }  (1 ≦ i ≦ Q)
#0 ≦ x_i ≦ 10^{18}  (1 ≦ i ≦ Q)
#There is at least one i (1 ≦ i ≦ Q) such that t_i = 2.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#Q
#t_1 x_1
#.
#.
#.
#t_{Q} x_{Q}
#
#Output
#For each query with t_i = 2, print the response in one line. It is guaranteed that there is at least one such query.
#
#Sample Input 1
#4
#1 1048577
#1 1
#2 2097153
#2 3
#
#Sample Output 1
#1048577
#-1
#We have x_1 mod N = 1, so the first query sets A_1 = 1048577.
#In the second query, initially we have h = x_2, for which A_{h mod N} = A_{1} ≠ -1, so we add 1 to h. Now we have A_{h mod N} = A_{2} = -1, so this query sets A_2 = 1.
#In the third query, we print A_{x_3 mod N} = A_{1} = 1048577.
#In the fourth query, we print A_{x_4 mod N} = A_{3} = -1.
#Note that, in this problem, N = 2^{20} = 1048576 is a constant and not given in input.

def 