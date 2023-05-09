Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    l = list(S)
    for i in range(Q):
        if T[i] == 1:
            l[A[i]-1], l[B[i]-1] = l[B[i]-1], l[A[i]-1]
        else:
            l[0:N], l[N:2*N] = l[N:2*N], l[0:N]
    print("".join(l))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    # FLIP
    first = S[:N]
    last = S[N:]

    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N and B[i] <= N:
                first = first[:A[i]-1] + last[B[i]-1] + first[A[i]:]
                last = last[:B[i]-1] + first[A[i]-1] + last[B[i]:]
            elif A[i] > N and B[i] > N:
                first = first[:A[i]-1-N] + last[B[i]-1-N] + first[A[i]-N:]
                last = last[:B[i]-1-N] + first[A[i]-1-N] + last[B[i]-N:]
            else:
                first = last[:B[i]-1-N] + first[A[i]-1] + last[B[i]-N:]
                last = first[:A[i]-1] + last[B[i]-1] + first[A[i]:]
        elif T[i] == 2:
            first, last = last, first

    print(first + last)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    for i in range(Q):
        if T[i] == 1:
            if A[i] < N:
                if B[i] < N:
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                else:
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]]
            else:
                if B[i] < N:
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[B[i]+1:]
                else:
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]]
        else:
            S = S[N:] + S[:N]

    print(S)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = s[:n]
    s2 = s[n:]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n:
                a -= 1
                b -= 1
                s1 = s1[:a] + s2[b] + s1[a+1:]
                s2 = s2[:b] + s1[a] + s2[b+1:]
            else:
                a -= n
                b -= n
                s2 = s2[:a] + s1[b] + s2[a+1:]
                s1 = s1[:b] + s2[a] + s1[b+1:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)

=======
Suggestion 5

def flip(s):
    n = len(s)
    s1 = s[:n//2]
    s2 = s[n//2:]
    return s2 + s1

n = int(input())
s = input()
q = int(input())

for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a-1, b-1
    if t == 1:
        s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else:
        s = flip(s)
print(s)

=======
Suggestion 6

def swap(string, index1, index2):
    string = list(string)
    string[index1-1], string[index2-1] = string[index2-1], string[index1-1]
    return ''.join(string)

=======
Suggestion 7

def swap(s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(N, S, Q, query)
    first = S[:N]
    last = S[N:]
    for i in range(Q):
        if query[i][0] == 1:
            if query[i][1] <= N and query[i][2] <= N:
                first = first[:query[i][1] - 1] + last[query[i][2] - 1] + first[query[i][1]:]
                last = last[:query[i][2] - 1] + first[query[i][1] - 1] + last[query[i][2]:]
            elif query[i][1] <= N and query[i][2] > N:
                first = first[:query[i][1] - 1] + last[query[i][2] - 1 - N] + first[query[i][1]:]
                last = last[:query[i][2] - 1 - N] + first[query[i][1] - 1] + last[query[i][2] - N:]
            elif query[i][1] > N and query[i][2] <= N:
                first = first[:query[i][1] - 1 - N] + last[query[i][2] - 1] + first[query[i][1] - N:]
                last = last[:query[i][2] - 1] + first[query[i][1] - 1 - N] + last[query[i][2]:]
            else:
                first = first[:query[i][1] - 1 - N] + last[query[i][2] - 1 - N] + first[query[i][1] - N:]
                last = last[:query[i][2] - 1 - N] + first[query[i][1] - 1 - N] + last[query[i][2] - N:]
        else:
            first, last = last, first
    print(first + last)

=======
Suggestion 9

def main():
    import sys
    import io
    import time

    #input
    def input():
        return sys.stdin.readline().rstrip()
    #N = int(input())
    #S = input()
    #Q = int(input())
    #T = [0]*Q
    #A = [0]*Q
    #B = [0]*Q
    #for i in range(Q):
    #    T[i], A[i], B[i] = map(int, input().split())
    N = 2
    S = 'FLIP'
    Q = 2
    T = [2, 1]
    A = [0, 1]
    B = [0, 4]
    #N = 2
    #S = 'FLIP'
    #Q = 6
    #T = [1, 2, 1, 1, 2, 1]
    #A = [1, 0, 1, 2, 0, 1]
    #B = [3, 0, 2, 3, 0, 4]
    #N = 2
    #S = 'FLIP'
    #Q = 10
    #T = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #A = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #B = [0, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    #N = 2
    #S = 'FLIP'
    #Q = 3
    #T = [1, 1, 1]
    #A = [1, 2, 3]
    #B = [2, 3, 4]
    #N = 2
    #S = 'FLIP'
    #Q = 3
    #T = [1, 1, 1]
    #A = [1, 2, 3]
    #B = [2, 3, 4]
    #N = 2
    #S = 'FLIP'

=======
Suggestion 10

def flip(S):
    return S[N:] + S[:N]
