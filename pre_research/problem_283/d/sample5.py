#Problem Statement
#A string consisting of lowercase English letters, (, and ) is said to be a good string if you can make it an empty string by the following procedure:
#First, remove all lowercase English letters.
#Then, repeatedly remove consecutive () while possible.
#For example, ((a)ba) is a good string, because removing all lowercase English letters yields (()), from which we can remove consecutive () at the 2-nd and 
#3-rd characters to obtain (), which in turn ends up in an empty string.
#You are given a good string S. We denote by S_i the i-th character of S.
#For each lowercase English letter a, b, …, and z, we have a ball with the letter written on it. Additionally, we have an empty box.
#For each i=1,2,… ,∣S∣ in this order, Takahashi performs the following operation unless he faints.
#If S_i is a lowercase English letter, put the ball with the letter written on it into the box. If the ball is already in the box, he faints.
#If S_i is (, do nothing.
#If S_i is ), take the maximum integer j less than i such that the j-th through i-th characters of S form a good string. (We can prove that such an integer 
#j always exists.) Take out from the box all the balls that he has put in the j-th through i-th operations.
#Determine if Takahashi can complete the sequence of operations without fainting.
#
#Constraints
#1≤∣S∣≤3×10^5
#S is a good string.
#
#Input
#The input is given from Standard Input in the following format:
#S
#
#Output
#Print Yes if he can complete the sequence of operations without fainting; print No otherwise.
#
#Sample Input 1
#((a)ba)
#
#Sample Output 1
#Yes
#
#Sample Input 2
#(a(ba))
#
#Sample Output 2
#No
#
#Sample Input 3
#(((())))
#
#Sample Output 3
#Yes
#
#Sample Input 4
#abca
#
#Sample Output 4
#No

def main():
    S = input()
    N = len(S)
    print(N)

if __name__ == '__main__':
    main()