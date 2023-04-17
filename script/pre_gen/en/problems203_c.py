#Problem Statement
#There are 10^{100}+1 villages, labeled with numbers 0, 1, ..., 10^{100}.
#For every integer i between 0 and 10^{100}-1 (inclusive), you can pay 1 yen (the currency) in Village i to get to Village (i + 1).
#There is no other way to travel between villages.
#Taro has K yen and is in Village 0 now. He will try to get to a village labeled with as large a number as possible.
#He has N friends. The i-th friend, who is in Village A_i, will give Taro B_i yen when he reaches Village A_i.
#Find the number with which the last village he will reach is labeled.
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#1 ≦ K ≦ 10^9
#1 ≦ A_i ≦ 10^{18}
#1 ≦ B_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#A_1 B_1
#:
#A_N B_N
#
#Output
#Print the answer.
#
#Sample Input 1
#2 3
#2 1
#5 10
#
#Sample Output 1
#4
#Takahashi will travel as follows:
#Go from Village 0 to Village 1, for 1 yen. Now he has 2 yen.
#Go from Village 1 to Village 2, for 1 yen. Now he has 1 yen.
#Get 1 yen from the 1-st friend in Village 2. Now he has 2 yen.
#Go from Village 2 to Village 3, for 1 yen. Now he has 1 yen.
#Go from Village 3 to Village 4, for 1 yen. Now he has 0 yen, and he has no friends in this village, so his journey ends here.
#Thus, we should print 4.
#
#Sample Input 2
#5 1000000000
#1 1000000000
#2 1000000000
#3 1000000000
#4 1000000000
#5 1000000000
#
#Sample Output 2
#6000000000
#Note that the answer may not fit into a 32-bit integer.
#
#Sample Input 3
#3 2
#5 5
#2 1
#2 2
#
#Sample Output 3
#10
#He may have multiple friends in the same village.

def 