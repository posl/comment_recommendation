Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    for i in range(1, M - N + 2):
        for j in range(i + 1, M - N + 3):
            for k in range(j + 1, M - N + 4):
                print(i, j, k)

main()

=======
Suggestion 2

def dfs(x, N, M):
    if x == N:
        print(*A)
        return
    for i in range(A[x-1]+1, M+1):
        A[x] = i
        dfs(x+1, N, M)

N, M = map(int, input().split())
A = [0] * N
dfs(0, N, M)

=======
Suggestion 3

def print_sequences(N,M):
    if N==1:
        for i in range(1,M+1):
            print(i)
    else:
        for i in range(1,M+1):
            for sequence in print_sequences(N-1,M-i):
                print(i,*sequence)

=======
Suggestion 4

def dfs(N,M,seq):
    if len(seq) == N:
        print(' '.join(map(str, seq)))
        return
    for i in range(1,M+1):
        if len(seq) == 0 or seq[-1] < i:
            seq.append(i)
            dfs(N,M,seq)
            seq.pop()

=======
Suggestion 5

def dfs(A, N, M, i):
    if i == N:
        print(' '.join(map(str, A)))
        return
    for j in range(1, M+1):
        if i == 0 or A[i-1] < j:
            A[i] = j
            dfs(A, N, M, i+1)

=======
Suggestion 6

def f(N, M, L):
    if N == 0:
        print(*L)
        return
    for i in range(1, M+1):
        if L and L[-1] >= i:
            continue
        f(N-1, M, L+[i])

N, M = map(int, input().split())
f(N, M, [])

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        if N == 1:
            print(i)
        else:
            search(i,i+1,N,M)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        dfs(n - 1, i, str(i))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        dfs(N, M, i, [i])

=======
Suggestion 10

def makeSeqs(N, M, i, seq):
    if i == N:
        print(*seq)
        return
    for j in range(1, M+1):
        if i == 0 or seq[i-1] < j:
            seq[i] = j
            makeSeqs(N, M, i+1, seq)

N, M = map(int, input().split())
makeSeqs(N, M, 0, [0]*N)
