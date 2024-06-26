#Problem Statement
#Snuke loves "paper cutting": he cuts out characters from a newspaper headline and rearranges them to form another string.
#He will receive a headline which contains one of the strings S_1,...,S_n tomorrow.
#He is excited and already thinking of what string he will create.
#Since he does not know the string on the headline yet, he is interested in strings that can be created regardless of which string the headline contains.
#Find the longest string that can be created regardless of which string among S_1,...,S_n the headline contains.
#If there are multiple such strings, find the lexicographically smallest one among them.
#
#Constraints
#1 ≦ n ≦ 50
#1 ≦ |S_i| ≦ 50 for every i = 1, ..., n.
#S_i consists of lowercase English letters (a - z) for every i = 1, ..., n.
#
#Input
#Input is given from Standard Input in the following format:
#n
#S_1
#...
#S_n
#
#Output
#Print the lexicographically smallest string among the longest strings that satisfy the condition.
#If the answer is an empty string, print an empty line.
#
#Sample Input 1
#3
#cbaa
#daacc
#acacac
#
#Sample Output 1
#aac
#The strings that can be created from each of cbaa, daacc and acacac, are aa, aac, aca, caa and so forth.
#Among them, aac, aca and caa are the longest, and the lexicographically smallest of these three is aac.
#
#Sample Input 2
#3
#a
#aa
#b
#
#Sample Output 2
#The answer is an empty string.

def 