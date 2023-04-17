#Problem Statement
#There are non-negative integers A, B, C, D, E, and F, which satisfy A× B× C≧ D× E× F.
#Find the remainder when (A× B× C)-(D× E× F) is divided by 998244353.
#
#Constraints
#0≦ A,B,C,D,E,F≦ 10^{18}
#A× B× C≧ D× E× F
#A, B, C, D, E, and F are integers.
#
#Input
#The input is given from Standard Input in the following format:
#A B C D E F
#
#Output
#Print the remainder when (A× B× C)-(D× E× F) is divided by 998244353, as an integer.
#
#Sample Input 1
#2 3 5 1 2 4
#
#Sample Output 1
#22
#Since A× B× C=2× 3× 5=30 and D× E× F=1× 2× 4=8,
#we have (A× B× C)-(D× E× F)=22. Divide this by 998244353 and print the remainder, which is 22.
#
#Sample Input 2
#1 1 1000000000 0 0 0
#
#Sample Output 2
#1755647
#Since A× B× C=1000000000 and D× E× F=0,
#we have (A× B× C)-(D× E× F)=1000000000. Divide this by 998244353 and print the remainder, which is 1755647.
#
#Sample Input 3
#1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
#
#Sample Output 3
#0
#We have (A× B× C)-(D× E× F)=0. Divide this by 998244353 and print the remainder, which is 0.

def 