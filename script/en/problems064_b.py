#Problem Statement
#It is only six months until Christmas, and AtCoDeer the reindeer is now planning his travel to deliver gifts.
#There are N houses along TopCoDeer street. The i-th house is located at coordinate a_i. He has decided to deliver gifts to all these houses.
#Find the minimum distance to be traveled when AtCoDeer can start and end his travel at any positions.  
#
#Constraints
#1 ≤ N ≤ 100
#0 ≤ a_i ≤ 1000
#a_i is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 a_2 ... a_N
#
#Output
#Print the minimum distance to be traveled.  
#
#Sample Input 1
#4
#2 3 7 9
#
#Sample Output 1
#7
#The travel distance of 7 can be achieved by starting at coordinate 9 and traveling straight to coordinate 2.
#It is not possible to do with a travel distance of less than 7, and thus 7 is the minimum distance to be traveled.  
#
#Sample Input 2
#8
#3 1 4 1 5 9 2 6
#
#Sample Output 2
#8
#There may be more than one house at a position.  

def 