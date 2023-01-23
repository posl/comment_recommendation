#Problem Statement
#You are given a sequence of non-negative integers A=(a_1,a_2,…,a_N).
#Let S be the set of non-negative integers that can be the sum of K terms in A (with distinct indices).
#Find the greatest multiple of D in S. If there is no multiple of D in S, print -1 instead.
#
#Constraints
#1≤K≤N≤100
#1≤D≤100
#0≤a_i≤10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N K D
#a_1 … a_N
#
#Output
#Print the answer.
#
#Sample Input 1
#4 2 2
#1 2 3 4
#
#Sample Output 1
#6
#
#Sample Input 2
#3 1 2
#1 3 5
#
#Sample Output 2
#-1

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(i + 1, n):
            s.add(a[i] + a[j])
    s = sorted(s, reverse=True)
    for i in range(len(s)):
        if s[i] % d == 0:
            print(s[i])
            return
    print(-1)

if __name__ == '__main__':
    main()