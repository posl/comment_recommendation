#Problem Statement
#Serval is fighting with a monster.
#The health of the monster is H.
#In one attack, Serval can decrease the monster's health by A.
#There is no other way to decrease the monster's health.
#Serval wins when the monster's health becomes 0 or below.
#Find the number of attacks Serval needs to make before winning.
#
#Constraints
#1 ≦ H ≦ 10^4
#1 ≦ A ≦ 10^4
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#H A
#
#Output
#Print the number of attacks Serval needs to make before winning.
#
#Sample Input 1
#10 4
#
#Sample Output 1
#3
#After one attack, the monster's health will be 6.
#After two attacks, the monster's health will be 2.
#After three attacks, the monster's health will be -2.
#Thus, Serval needs to make three attacks to win.
#
#Sample Input 2
#1 10000
#
#Sample Output 2
#1
#
#Sample Input 3
#10000 1
#
#Sample Output 3
#10000

def 