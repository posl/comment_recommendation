#Problem Statement
#A shop sells N kinds of lunchboxes, one for each kind.
#For each i = 1, 2, ..., N, the i-th kind of lunchbox contains A_i takoyaki (octopus balls) and B_i taiyaki (fish-shaped cakes).
#Takahashi wants to eat X or more takoyaki and Y or more taiyaki.
#Determine whether it is possible to buy some number of lunchboxes to get at least X takoyaki and at least Y taiyaki. If it is possible, find the minimum number of lunchboxes that Takahashi must buy to get them.
#Note that just one lunchbox is in stock for each kind; you cannot buy two or more lunchboxes of the same kind.
#
#Constraints
#1 ≦ N ≦ 300
#1 ≦ X, Y ≦ 300
#1 ≦ A_i, B_i ≦ 300
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#X Y
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_N B_N
#
#Output
#If Takahashi cannot get at least X takoyaki and at least Y taiyaki, print -1; otherwise, print the minimum number of lunchboxes that he must buy to get them.
#
#Sample Input 1
#3
#5 6
#2 1
#3 4
#2 3
#
#Sample Output 1
#2
#He wants to eat 5 or more takoyaki and 6 or more taiyaki.
#Buying the second and third lunchboxes will get him 3 + 2 = 5 taiyaki and 4 + 3 = 7 taiyaki.
#
#Sample Input 2
#3
#8 8
#3 4
#2 3
#2 1
#
#Sample Output 2
#-1
#Even if he is to buy every lunchbox, it is impossible to get at least 8 takoyaki and at least 8 taiyaki.
#Thus, print -1.

def 