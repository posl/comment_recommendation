Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [0] * n
    def dfs(i):
        if i == n:
            print(' '.join(map(str, a)))
        else:
            for j in range(1, m + 1):
                a[i] = j
                dfs(i + 1)
    dfs(0)

=======
Suggestion 2

def increasing_sequence(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        return [[i]+s for i in range(1, m+1) for s in increasing_sequence(n-1, m) if i < s[0]]

=======
Suggestion 3

def increasing_sequence(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [ [i] + s for i in range(1, m + 1) for s in increasing_sequence(n - 1, i - 1)]

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    #print(N, M)
    for i in range(1, M+1):
        if N == 1:
            print(i)
        else:
            for j in range(1, M+1):
                if N == 2:
                    if i < j:
                        print(i, j)
                else:
                    for k in range(1, M+1):
                        if N == 3:
                            if j < k:
                                print(i, j, k)
                        else:
                            for l in range(1, M+1):
                                if N == 4:
                                    if k < l:
                                        print(i, j, k, l)
                                else:
                                    for m in range(1, M+1):
                                        if N == 5:
                                            if l < m:
                                                print(i, j, k, l, m)
                                        else:
                                            for n in range(1, M+1):
                                                if N == 6:
                                                    if m < n:
                                                        print(i, j, k, l, m, n)
                                                else:
                                                    for o in range(1, M+1):
                                                        if N == 7:
                                                            if n < o:
                                                                print(i, j, k, l, m, n, o)
                                                        else:
                                                            for p in range(1, M+1):
                                                                if N == 8:
                                                                    if o < p:
                                                                        print(i, j, k, l, m, n, o, p)
                                                                else:
                                                                    for q in range(1, M+1):
                                                                        if N == 9:
                                                                            if p < q:
                                                                                print(i, j, k, l, m, n, o, p, q)
                                                                        else:
                                                                            for r in range(1, M+1):
                                                                                if N == 10:
                                                                                    if q < r:
                                                                                        print(i, j, k, l, m, n, o, p, q, r)
    return 0

=======
Suggestion 5

def rec(i, N, M, seq):
    if i == N:
        print(' '.join(map(str, seq)))
        return
    for j in range(seq[i-1]+1, M+1):
        seq[i] = j
        rec(i+1, N, M, seq)

=======
Suggestion 6

def printSequences(n, m, sequence):
    if n == 0:
        print(sequence)
        return
    if n > 0:
        for i in range(1, m+1):
            printSequences(n-1, m, sequence + str(i) + " ")
    return

n, m = map(int, input().split())
printSequences(n, m, "")

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        print(i,end=" ")
    print()
    for i in range(1,M):
        if i%2==0:
            print(i,end=" ")
    print(M)
    for i in range(1,M):
        if i%2==1:
            print(i,end=" ")
    print(M)

=======
Suggestion 8

def print_all_increasing_sequences(n, m, s="", i=1):
    if len(s) == n:
        print(s)
        return
    while i <= m:
        print_all_increasing_sequences(n, m, s + str(i), i + 1)
        i += 1
    return

=======
Suggestion 9

def print_list(l):
    for i in l:
        print(i, end=' ')
    print()

=======
Suggestion 10

def func():
    pass
