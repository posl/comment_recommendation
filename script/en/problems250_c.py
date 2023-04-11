#Problem Statement
#N balls are lined up in a row from left to right.  Initially, the i-th (1 ≦ i ≦ N) ball from the left has an integer i written on it.
#Takahashi has performed Q operations.  The i-th (1 ≦ i ≦ Q) operation was as follows.
#Swap the ball with the integer x_i written on it with the next ball to the right.  If the ball with the integer x_i written on it was originally the rightmost ball, swap it with the next ball to the left instead.
#Let a_i be the integer written on the i-th (1 ≦ i ≦ N) ball after the operations.  Find a_1,...,a_N.
#
#Constraints
#2 ≦ N ≦ 2 × 10^5
#1 ≦ Q ≦ 2 × 10^5
#1 ≦ x_i ≦ N
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N Q
#x_1
#.
#.
#.
#x_Q
#
#Output
#Print a_1,...,a_N, with spaces in between.
#
#Sample Input 1
#5 5
#1
#2
#3
#4
#5
#
#Sample Output 1
#1 2 3 5 4
#The operations are performed as follows.  
#Swap the ball with 1 written on it with the next ball to the right.  Now, the balls have integers 2,1,3,4,5 written on them, from left to right.
#Swap the ball with 2 written on it with the next ball to the right.  Now, the balls have integers 1,2,3,4,5 written on them, from left to right.
#Swap the ball with 3 written on it with the next ball to the right.  Now, the balls have integers 1,2,4,3,5 written on them, from left to right.
#Swap the ball with 4 written on it with the next ball to the right.  Now, the balls have integers 1,2,3,4,5 written on them, from left to right.
#Swap the ball with 5 written on it with the next ball to the left, since it is the rightmost ball.  Now, the balls have integers 1,2,3,5,4 written on them, from left to right.
#
#Sample Input 2
#7 7
#7
#7
#7
#7
#7
#7
#7
#
#Sample Output 2
#1 2 3 4 5 7 6
#
#Sample Input 3
#10 6
#1
#5
#2
#9
#6
#6
#
#Sample Output 3
#1 2 3 4 5 7 6 8 10 9

def 