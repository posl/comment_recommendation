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
    S = input()
    ans = "Yes"
    if S[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans = "No"
    if S[-1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans = "No"
    if S[1:-1].isdigit() == False:
        ans = "No"
    if len(S[1:-1]) != 6:
        ans = "No"
    if int(S[1:-1]) < 100000 or int(S[1:-1]) > 999999:
        ans = "No"
    print(ans)

if __name__ == '__main__':
    main()