#Problem Statement
#There are N items in a shop. For each i = 1, 2, ..., N, the price of the i-th item is A_i yen (the currency of Japan).
#Takahashi has K coupons.
#Each coupon can be used on one item. You can use any number of coupons, possibly zero, on the same item. Using k coupons on an item with a price of a yen allows you to buy it for max{a - kX, 0} yen.
#Print the minimum amount of money Takahashi needs to buy all the items.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ K, X ≦ 10^9
#1 ≦ A_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K X
#A_1 A_2 ... A_N
#
#Output
#Print the answer.
#
#Sample Input 1
#5 4 7
#8 3 10 5 13
#
#Sample Output 1
#12
#By using 1 coupon on the 1-st item, 1 coupon on the 3-rd item, and 2 coupons on the 5-th item, Takahashi can:
#buy the 1-st item for max{A_1-X, 0 } = 1 yen,
#buy the 2-nd item for max{A_2, 0 } = 3 yen,
#buy the 3-rd item for max{A_3-X, 0 } = 3 yen,
#buy the 4-th item for max{A_4, 0 } = 5 yen,
#buy the 5-th item for max{A_5-2X, 0 } = 0 yen,
#for a total of 1 + 3 + 3 + 5 + 0 = 12 yen, which is the minimum possible.
#
#Sample Input 2
#5 100 7
#8 3 10 5 13
#
#Sample Output 2
#0
#
#Sample Input 3
#20 815 60
#2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202
#
#Sample Output 3
#112

def 