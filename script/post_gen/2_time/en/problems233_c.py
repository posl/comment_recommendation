#Problem Statement
#We have N bags.
#Bag i contains L_i balls. The j-th ball (1≦ j≦ L_i) in Bag i has a positive integer a_{i,j} written on it.
#We will pick out one ball from each bag.
#How many ways are there to pick the balls so that the product of the numbers written on the picked balls is X?
#Here, we distinguish all balls, even with the same numbers written on them.
#
#Constraints
#N ≧ 2
#L_i ≧ 2
#The product of the numbers of balls in the bags is at most 10^5: prod_{i=1}^{N}L_i ≦ 10^5.
#1 ≦ a_{i,j} ≦ 10^9
#1 ≦ X ≦ 10^{18}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N X
#L_1 a_{1,1} a_{1,2} ... a_{1,L_1}
#L_2 a_{2,1} a_{2,2} ... a_{2,L_2}
#.
#.
#.
#L_N a_{N,1} a_{N,2} ... a_{N,L_N}
#
#Output
#Print the answer. 
#
#Sample Input 1
#2 40
#3 1 8 4
#2 10 5
#
#Sample Output 1
#2
#When choosing the 3-rd ball in Bag 1 and 1-st ball in Bag 2, we have a_{1,3} × a_{2,1} = 4 × 10 = 40.
#When choosing the 2-nd ball in Bag 1 and 2-nd ball in Bag 2, we have a_{1,2} × a_{2,2} = 8 × 5 = 40.
#There are no other ways to make the product 40, so the answer is 2.
#
#Sample Input 2
#3 200
#3 10 10 10
#3 10 10 10
#5 2 2 2 2 2
#
#Sample Output 2
#45
#Note that we distinguish all balls, even with the same numbers written on them.
#
#Sample Input 3
#3 1000000000000000000
#2 1000000000 1000000000
#2 1000000000 1000000000
#2 1000000000 1000000000
#
#Sample Output 3
#0
#There may be no way to make the product X.

def 