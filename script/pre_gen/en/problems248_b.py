#Problem Statement
#There are A slimes.
#Each time Snuke shouts, the slimes multiply by K times.
#In order to have B or more slimes, at least how many times does Snuke need to shout?
#
#Constraints
#1 ≦ A ≦ B ≦ 10^9
#2 ≦ K ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B K
#
#Output
#Print the answer.
#
#Sample Input 1
#1 4 2
#
#Sample Output 1
#2
#We start with one slime.
#After Snuke's first shout, we have two slimes; after his second shout, we have four slimes. Thus, he needs to shout at least twice to have four or more slimes.
#
#Sample Input 2
#7 7 10
#
#Sample Output 2
#0
#We have seven slimes already at the start.
#
#Sample Input 3
#31 415926 5
#
#Sample Output 3
#6

def 