#Problem Statement
#It is November 18 now in Japan. By the way, 11 and 18 are adjacent Lucas numbers.
#You are given an integer N. Find the N-th Lucas number.
#Here, the i-th Lucas number L_i is defined as follows:
#L_0=2
#L_1=1
#L_i=L_{i-1}+L_{i-2} (i≥2)
#
#Constraints
#1≤N≤86
#It is guaranteed that the answer is less than 10^{18}.
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the N-th Lucas number.
#
#Sample Input 1
#5
#
#Sample Output 1
#11
#L_0=2
#L_1=1
#L_2=L_0+L_1=3
#L_3=L_1+L_2=4
#L_4=L_2+L_3=7
#L_5=L_3+L_4=11
#Thus, the 5-th Lucas number is 11.
#
#Sample Input 2
#86
#
#Sample Output 2
#939587134549734843

def 