#Problem Statement
#AtCoder Grand Contest (AGC), a regularly held contest with a world authority, has been held 54 times.
#Just like the 230-th ABC ― the one you are in now ― is called ABC230, the N-th AGC is initially named with a zero-padded 3-digit number N. (The 1-st AGC is AGC001, the 2-nd AGC is AGC002, ...)
#However, the latest 54-th AGC is called AGC055, where the number is one greater than 54. Because AGC042 is canceled and missing due to the social situation, the 42-th and subsequent contests are assigned numbers that are one greater than the numbers of contests held. (See also the explanations at Sample Inputs and Outputs.)
#Here is the problem: given an integer N, print the name of the N-th AGC in the format AGCXXX, where XXX is the zero-padded 3-digit number.
#
#Constraints
#1 ≦ N ≦ 54
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the name of the N-th AGC in the specified format.
#
#Sample Input 1
#42
#
#Sample Output 1
#AGC043
#As explained in Problem Statement, the 42-th and subsequent AGCs are assigned numbers that are one greater than the numbers of contests.
#Thus, the 42-th AGC is named AGC043.
#
#Sample Input 2
#19
#
#Sample Output 2
#AGC019
#The 41-th and preceding AGCs are assigned numbers that are equal to the numbers of contests.
#Thus, the answer is AGC019.
#
#Sample Input 3
#1
#
#Sample Output 3
#AGC001
#As mentioned in Problem Statement, the 1-st AGC is named AGC001.
#Be sure to pad the number with zeros into a 3-digit number.
#
#Sample Input 4
#50
#
#Sample Output 4
#AGC051

def 