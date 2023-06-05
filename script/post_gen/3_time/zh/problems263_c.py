Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = list(range(1,m+1))
    for i in range(1,n):
        a = [x for x in a if x < m-n+i+1]
    print(a)

=======
Suggestion 2

def print_sequence(n, m, sequence):
    if len(sequence) == n:
        print(" ".join(map(str, sequence)))
    else:
        for i in range(1, m + 1):
            if i not in sequence:
                print_sequence(n, m, sequence + [i])

=======
Suggestion 3

def printSequence(n, m):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        result = []
        for i in range(1, m+1):
            for j in printSequence(n-1, i):
                result.append([i]+j)
        return result

=======
Suggestion 4

def get_next(seq, n, m):
    if len(seq) == n:
        print(*seq)
    else:
        for i in range(seq[-1]+1, m+1):
            get_next(seq+[i], n, m)

=======
Suggestion 5

def dfs(N,M,now):
    if len(now)==N:
        print(*now)
        return
    for i in range(now[-1]+1,M+1):
        dfs(N,M,now+[i])

N,M=map(int,input().split())
for i in range(1,M+1):
    dfs(N,M,[i])

=======
Suggestion 6

def print_seq(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, m+1):
        if len(seq) == 0 or i > seq[-1]:
            print_seq(n, m, seq + [i])

=======
Suggestion 7

def print_sequence(n,m):
    if n == 0:
        print()
    elif n == 1:
        for i in range(1,m+1):
            print(i)
    else:
        for i in range(n,m+1):
            print_sequence(n-1,i-1)

n,m = map(int,input().split())
print_sequence(n,m)

=======
Suggestion 8

def f(n,m):
    if n==1:
        return [[i] for i in range(1,m+1)]
    else:
        return [ [i]+j for i in range(1,m+1) for j in f(n-1,m) if i<j[0] ]

n,m=map(int,input().split())
for i in f(n,m):
    print(*i)

=======
Suggestion 9

def dfs(N, M, arr, i, j):
    if i == N:
        print(' '.join(map(str, arr)))
        return
    for k in range(j+1, M+1):
        arr[i] = k
        dfs(N, M, arr, i+1, k)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = [1]*n
    while True:
        for i in range(n):
            print(a[i],end=' ')
        print()
        i = n-1
        while i>=0 and a[i] == m:
            i -= 1
        if i<0:
            break
        a[i] += 1
        for j in range(i+1,n):
            a[j] = a[i]
