#Problem Statement
#Takahashi is going to read a manga series "Snuke-kun" in 10^9 volumes.
#Initially, Takahashi has N books of this series.  The i-th book is Volume a_i.  
#Takahashi may repeat the following operation any number of (possibly zero) times only before he begins to read:
#Do nothing if he has 1 or less books; otherwise, sell two of the books he has and buy one book of any volume instead.
#Then, Takahashi reads Volume 1, Volume 2, Volume 3, ..., in order.  However, when he does not have a book of the next volume to read, he stops reading the series (regardless of the other volumes he has).  
#Find the latest volume of the series that he can read up to.  If he cannot read any, let the answer be 0.
#
#Constraints
#1 ≦ N ≦ 3 × 10^5
#1 ≦ a_i ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#a_1 ... a_N
#
#Output
#Print the answer.
#
#Sample Input 1
#6
#1 2 4 6 7 271
#
#Sample Output 1
#4
#Before he begins to read the series, he may do the following operation: "sell books of Volumes 7 and 271 and buy one book of Volume 3 instead."  Then, he has one book each of Volumes 1, 2, 3, 4, and 6.
#If he then begins to read the series, he reads Volumes 1, 2, 3, and 4, then tries to read Volume 5.  However, he does not have one, so he stops reading at this point.
#Regardless of the choices in the operation, he cannot read Volume 5, so the answer is 4.
#
#Sample Input 2
#10
#1 1 1 1 1 1 1 1 1 1
#
#Sample Output 2
#5
#Takahashi may have multiple books of the same volume.
#For this input, if he performs the following 4 operations before he begins to read the series, he can read up to Volume 5, which is the maximum:
#Sell two books of Volume 1 and buy a book of Volume 2 instead.
#Sell two books of Volume 1 and buy a book of Volume 3 instead.
#Sell two books of Volume 1 and buy a book of Volume 4 instead.
#Sell two books of Volume 1 and buy a book of Volume 5 instead.
#
#Sample Input 3
#1
#5
#
#Sample Output 3
#0
#Takahashi cannot read Volume 1.

def 