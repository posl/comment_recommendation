#Problem Statement
#Snuke signed up for a new website which holds programming competitions.
#He worried that he might forget his password, and he took notes of it.
#Since directly recording his password would cause him trouble if stolen,
#he took two notes: one contains the characters at the odd-numbered positions, and the other contains the characters at the even-numbered positions.
#You are given two strings O and E. O contains the characters at the odd-numbered positions retaining their relative order, and E contains the characters at the even-numbered positions retaining their relative order.
#Restore the original password.
#
#Constraints
#O and E consists of lowercase English letters (a - z).
#1 ≦ |O|,|E| ≦ 50
#|O| - |E| is either 0 or 1.
#
#Input
#Input is given from Standard Input in the following format:
#O
#E
#
#Output
#Print the original password.
#
#Sample Input 1
#xyz
#abc
#
#Sample Output 1
#xaybzc
#The original password is xaybzc. Extracting the characters at the odd-numbered positions results in xyz, and extracting the characters at the even-numbered positions results in abc.
#
#Sample Input 2
#atcoderbeginnercontest
#atcoderregularcontest
#
#Sample Output 2
#aattccooddeerrbreeggiunlnaerrccoonntteesstt

def 