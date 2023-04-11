#Problem Statement
#Takahashi is a member of a programming competition site, ButCoder.
#Each member of ButCoder is assigned two values: Inner Rating and Displayed Rating.
#The Displayed Rating of a member is equal to their Inner Rating if the member has participated in 10 or more contests. Otherwise, the Displayed Rating will be their Inner Rating minus 100 × (10 - K) when the member has participated in K contests.
#Takahashi has participated in N contests, and his Displayed Rating is R. Find his Inner Rating.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 100
#0 ≦ R ≦ 4111
#
#Input
#Input is given from Standard Input in the following format:
#N R
#
#Output
#Print his Inner Rating.
#
#Sample Input 1
#2 2919
#
#Sample Output 1
#3719
#Takahashi has participated in 2 contests, which is less than 10, so his Displayed Rating is his Inner Rating minus 100 × (10 - 2) = 800.
#Thus, Takahashi's Inner Rating is 2919 + 800 = 3719.
#
#Sample Input 2
#22 3051
#
#Sample Output 2
#3051

def 