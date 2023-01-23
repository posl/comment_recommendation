#Problem Statement
#You are given N strings S_1,S_2,…,S_N in this order.
#Print S_N,S_N−1,…,S_1 in this order.
#
#Constraints
#1≤N≤10
#N is an integer.
#S_i is a string of length between 1 and 10, inclusive, consisting of lowercase English letters, uppercase English letters, and digits.
#
#Input
#The input is given from Standard Input in the following format:
#N
#S_1
#S_2
#⋮
#S_N
#
#Output
#Print N lines. The i-th (1≤i≤N) line should contain S_N+1−i.
#
#Sample Input 1
#3
#Takahashi
#Aoki
#Snuke
#
#Sample Output 1
#Snuke
#Aoki
#Takahashi
#
#Sample Input 2
#4
#2023
#Year
#New
#Happy
#
#Sample Output 2
#Happy
#New
#Year
#2023

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

if __name__ == '__main__':
    main()