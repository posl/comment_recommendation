#Problem Statement
#There is an N× N grid with horizontal rows and vertical columns, where all squares are initially painted white. Let (i,j) denote the square at the i-th row and j-th column.
#Takahashi has integers A and B, which are between 1 and N (inclusive). He will do the following operations.
#For every integer k such that max(1-A,1-B)≦ k≦ min(N-A,N-B), paint (A+k,B+k) black.
#For every integer k such that max(1-A,B-N)≦ k≦ min(N-A,B-1), paint (A+k,B-k) black.
#In the grid after these operations, find the color of each square (i,j) such that P≦ i≦ Q and R≦ j≦ S.
#
#Constraints
#1 ≦ N ≦ 10^{18}
#1 ≦ A ≦ N
#1 ≦ B ≦ N
#1 ≦ P ≦ Q ≦ N
#1 ≦ R ≦ S ≦ N
#(Q-P+1)×(S-R+1)≦ 3× 10^5
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N A B
#P Q R S
#
#Output
#Print Q-P+1 lines.
#Each line should contain a string of length S-R+1 consisting of # and ..
#The j-th character of the string in the i-th line should be # to represent that (P+i-1, R+j-1) is painted black, and . to represent that (P+i-1, R+j-1) is white.  
#
#Sample Input 1
#5 3 2
#1 5 1 5
#
#Sample Output 1
#...#.
##.#..
#.#...
##.#..
#...#.
#The first operation paints the four squares (2,1), (3,2), (4,3), (5,4) black, and the second paints the four squares (4,1), (3,2), (2,3), (1,4) black.
#Thus, the above output should be printed, since P=1, Q=5, R=1, S=5.
#
#Sample Input 2
#5 3 3
#4 5 2 5
#
#Sample Output 2
##.#.
#...#
#The operations paint the nine squares (1,1), (1,5), (2,2), (2,4), (3,3), (4,2), (4,4), (5,1), (5,5).
#Thus, the above output should be printed, since P=4, Q=5, R=2, S=5.
#
#Sample Input 3
#1000000000000000000 999999999999999999 999999999999999999
#999999999999999998 1000000000000000000 999999999999999998 1000000000000000000
#
#Sample Output 3
##.#
#.#.
##.#
#Note that the input may not fit into a 32-bit integer type.

def 