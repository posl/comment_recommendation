#Problem Statement
#AtCoder City will hold a mayoral election. The candidates are Aoki and Takahashi.
#The city consists of N towns, the i-th of which has A_i pro-Aoki voters and B_i pro-Takahashi voters. There are no other voters.
#Takahashi can make a speech in each town.
#If he makes a speech in some town, all voters in that town, pro-Takahashi or pro-Aoki, will vote for Takahashi.
#On the other hand, if he does not make a speech in some town, the pro-Aoki voters in that town will vote for Aoki, and the pro-Takahashi voters will not vote.
#To get more votes than Aoki, in how many towns does Takahashi need to make speeches at least?
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 B_1
#.
#.
#.
#A_N B_N
#
#Output
#Print the answer.
#
#Sample Input 1
#4
#2 1
#2 2
#5 1
#1 3
#
#Sample Output 1
#1
#After making a speech in the third town, Aoki and Takahashi will get 5 and 6 votes, respectively.
#
#Sample Input 2
#5
#2 1
#2 1
#2 1
#2 1
#2 1
#
#Sample Output 2
#3
#After making speeches in three towns, Aoki and Takahashi will get 4 and 9 votes, respectively.
#
#Sample Input 3
#1
#273 691
#
#Sample Output 3
#1

def 