#Problem Statement
#You are given a string S consisting of uppercase English letters and digits. Determine whether S satisfies the following condition.
#S is a concatenation of the following characters and string in the order listed.
#An uppercase English letter
#A string of length 6 that is a decimal representation of an integer between 100000 and 999999, inclusive
#An uppercase English letter
#
#Constraints
#S consists of uppercase English letters and digits.
#The length of S is between 1 and 10, inclusive.
#
#Input
#The input is given from Standard Input in the following format:
#S
#
#Output
#If S satisfies the condition in the problem statement, print Yes; otherwise, print No.
#
#Sample Input 1
#Q142857Z
#
#Sample Output 1
#Yes
#
#Sample Input 2
#AB912278C
#
#Sample Output 2
#No
#
#Sample Input 3
#X900000
#
#Sample Output 3
#No
#
#Sample Input 4
#K012345K
#
#Sample Output 4
#No

def main():
    s = input()
    if len(s) != 10:
        print('No')
        return
    if s[0] == s[9] and s[1:7].isdigit() and 100000 <= int(s[1:7]) <= 999999:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()