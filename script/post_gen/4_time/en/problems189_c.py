#Problem Statement
#There are N dishes arranged in a row in front of Takahashi. The i-th dish from the left has A_i oranges on it.
#Takahashi will choose a triple of integers (l, r, x) satisfying all of the following conditions:
#1≦ l ≦ r ≦ N;
#1 ≦ x;
#for every integer i between l and r (inclusive), x ≦ A_i.
#He will then pick up and eat x oranges from each of the l-th through r-th dishes from the left.
#At most how many oranges can he eat by choosing the triple (l, r, x) to maximize this number?
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^4
#1 ≦ A_i ≦ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#
#Output
#Print the maximum number of oranges Takahashi can eat.
#
#Sample Input 1
#6
#2 4 4 9 4 9
#
#Sample Output 1
#20
#By choosing (l,r,x)=(2,6,4), he can eat 20 oranges.
#
#Sample Input 2
#6
#200 4 4 9 4 9
#
#Sample Output 2
#200
#By choosing (l,r,x)=(1,1,200), he can eat 200 oranges.

def 