#Problem Statement
#We will call a string that can be obtained by concatenating two equal strings an even string.
#For example, xyzxyz and aaaaaa are even, while ababab and xyzxy are not.
#You are given an even string S consisting of lowercase English letters.
#Find the length of the longest even string that can be obtained by deleting one or more characters from the end of S.
#It is guaranteed that such a non-empty string exists for a given input.
#
#Constraints
#2 ≦ |S| ≦ 200
#S is an even string consisting of lowercase English letters.
#There exists a non-empty even string that can be obtained by deleting one or more characters from the end of S.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the length of the longest even string that can be obtained.
#
#Sample Input 1
#abaababaab
#
#Sample Output 1
#6
#abaababaab itself is even, but we need to delete at least one character.
#abaababaa is not even.
#abaababa is not even.
#abaabab is not even.
#abaaba is even. Thus, we should print its length, 6.
#
#Sample Input 2
#xxxx
#
#Sample Output 2
#2
#xxx is not even.
#xx is even.
#
#Sample Input 3
#abcabcabcabc
#
#Sample Output 3
#6
#The longest even string that can be obtained is abcabc, whose length is 6.
#
#Sample Input 4
#akasakaakasakasakaakas
#
#Sample Output 4
#14
#The longest even string that can be obtained is akasakaakasaka, whose length is 14.

def 