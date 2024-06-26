#Problem Statement
#Given a string S, print AC if it perfectly matches Hello,World!; otherwise, print WA.
#What is a perfect match?Strings A is said to perfectly match B when the length of A is equal to that of B, and the i-th character of A is the same as the i-th character of B for every integer i such that 1 ≦ i ≦ |A|.
#
#Constraints
#1 ≦ |S| ≦ 15
#S consists of English lowercase letters, English uppercase letters, ,, and !.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the answer.
#
#Sample Input 1
#Hello,World!
#
#Sample Output 1
#AC
#The string S perfectly matches Hello,World!.
#
#Sample Input 2
#Hello,world!
#
#Sample Output 2
#WA
#The seventh character from the beginning should be an uppercase W in Hello,World!, but S has a lowercase w in that position. Thus, S does not match Hello,World!.
#
#Sample Input 3
#Hello!World!
#
#Sample Output 3
#WA

def 