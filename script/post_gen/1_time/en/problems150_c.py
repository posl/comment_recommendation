Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [i-1 for i in P]
    Q = [i-1 for i in Q]
    def fact(n):
        return 1 if n == 0 else n*fact(n-1)
    def find_index(permutation):
        index = 0
        for i in range(len(permutation)):
            index += permutation[i]*fact(len(permutation)-i-1)
            for j in range(i+1, len(permutation)):
                if permutation[i] > permutation[j]:
                    permutation[j] -= 1
        return index
    print(abs(find_index(P) - find_index(Q)))

=======
Suggestion 2

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

=======
Suggestion 3

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 4

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    P = tuple(P)
    Q = tuple(Q)
    P = (P[0],) + P[1:] + (N + 1,)
    Q = (Q[0],) + Q[1:] + (N + 1,)
    # print(P)
    # print(Q)
    P_index = 0
    Q_index = 0
    for i in range(1, N + 1):
        # print("i", i)
        for j in range(1, N + 1):
            # print("j", j)
            if P[i] > P[j]:
                P_index += 1
            if Q[i] > Q[j]:
                Q_index += 1
    # print(P_index)
    # print(Q_index)
    print(abs(P_index - Q_index))

=======
Suggestion 5

def perm2num(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = p[i]
        for j in range(i):
            if a[j] > a[i]:
                a[j] -= 1
    num = 0
    for i in range(n):
        num += a[i] * math.factorial(n - 1 - i)
    return num

=======
Suggestion 6

def  fact ( n ):
     if  n  <=   1 :
         return   1 
     else :
         return  n * fact( n  -   1 )

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # get lexicographically order
    def get_order(P):
        order = 0
        for i in range(N):
            count = 0
            for j in range(i + 1, N):
                if P[i] > P[j]:
                    count += 1
            order += count * math.factorial(N - i - 1)
        return order

    print(abs(get_order(P) - get_order(Q)))

import math
main()

=======
Suggestion 8

def permutation(N, P):
    P = list(P)
    perm = []
    for i in range(N):
        for j in range(N):
            if j not in perm:
                perm.append(j)
                break
    return perm

=======
Suggestion 9

def get_permutation(n, index):
    """Return the index-th permutation of (1,2,...,n)."""
    if n == 1:
        return [1]
    else:
        fact = 1
        for i in range(2, n):
            fact *= i
        remainder = index % fact
        quotient = index // fact
        if remainder == 0:
            quotient -= 1
            remainder = fact
        return [quotient + 1] + get_permutation(n - 1, remainder)
