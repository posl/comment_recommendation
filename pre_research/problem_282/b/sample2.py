#Problem Statement
#N participants, numbered 1 to N, will participate in a contest with M problems, numbered 1 to M.
#For an integer i between 1 and N and an integer j between 1 and M, participant i can solve problem j if the j-th character of S_i is o, and cannot solve it if that character is x.
#The participants must be in pairs. Print the number of ways to form a pair of participants who can collectively solve all the M problems.
#More formally, print the number of pairs (x,y) of integers satisfying 1≤x<y≤N such that for any integer j between 1 and M, at least one of participant 
#x and participant y can solve problem j.
#
#Constraints
#N is an integer between 2 and 30, inclusive.
#M is an integer between 1 and 30, inclusive.
#S_i is a string of length M consisting of o and x.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#S_1
#S_2
#⋮
#S_N
#
#Output
#Print the answer.
#
#Sample Input 1
#5 5
#ooooo
#oooxx
#xxooo
#oxoxo
#xxxxx
#
#Sample Output 1
#5
#
#Sample Input 2
#3 2
#ox
#xo
#xx
#
#Sample Output 2
#1
#
#Sample Input 3
#2 4
#xxxx
#oxox
#
#Sample Output 3
#0

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if all([S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()