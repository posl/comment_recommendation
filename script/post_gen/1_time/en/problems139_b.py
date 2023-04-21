#Problem Statement
#Takahashi's house has only one socket.
#Takahashi wants to extend it with some number of power strips, each with A sockets, into B or more empty sockets.
#One power strip with A sockets can extend one empty socket into A empty sockets.
#Find the minimum number of power strips required.
#
#Constraints
#All values in input are integers.
#2 ≦ A ≦ 20
#1 ≦ B ≦ 20
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print the minimum number of power strips required.
#
#Sample Input 1
#4 10
#
#Sample Output 1
#3
#3 power strips, each with 4 sockets, extend the socket into 10 empty sockets.
#
#Sample Input 2
#8 9
#
#Sample Output 2
#2
#2 power strips, each with 8 sockets, extend the socket into 15 empty sockets.
#
#Sample Input 3
#8 8
#
#Sample Output 3
#1

def 