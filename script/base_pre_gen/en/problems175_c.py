#Problem Statement
#Takahashi, who lives on the number line, is now at coordinate X. He will make exactly K moves of distance D in the positive or negative direction.
#More specifically, in one move, he can go from coordinate x to x + D or x - D.
#He wants to make K moves so that the absolute value of the coordinate of the destination will be the smallest possible.
#Find the minimum possible absolute value of the coordinate of the destination.
#
#Constraints
#-10^{15} ≦ X ≦ 10^{15}
#1 ≦ K ≦ 10^{15}
#1 ≦ D ≦ 10^{15}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#X K D
#
#Output
#Print the minimum possible absolute value of the coordinate of the destination.
#
#Sample Input 1
#6 2 4
#
#Sample Output 1
#2
#Takahashi is now at coordinate 6. It is optimal to make the following moves:
#Move from coordinate 6 to (6 - 4 =) 2.
#Move from coordinate 2 to (2 - 4 =) -2.
#Here, the absolute value of the coordinate of the destination is 2, and we cannot make it smaller.
#
#Sample Input 2
#7 4 3
#
#Sample Output 2
#1
#Takahashi is now at coordinate 7. It is optimal to make, for example, the following moves:
#Move from coordinate 7 to 4.
#Move from coordinate 4 to 7.
#Move from coordinate 7 to 4.
#Move from coordinate 4 to 1.
#Here, the absolute value of the coordinate of the destination is 1, and we cannot make it smaller.
#
#Sample Input 3
#10 1 2
#
#Sample Output 3
#8
#
#Sample Input 4
#1000000000000000 1000000000000000 1000000000000000
#
#Sample Output 4
#1000000000000000
#The answer can be enormous.

def 