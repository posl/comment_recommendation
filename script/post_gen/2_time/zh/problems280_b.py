Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0]*N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 2

def solution():
    n = int(input())
    s = list(map(int,input().split()))
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - s[i-1]
    print(" ".join(map(str,a)))

=======
Suggestion 3

def solve(n, s):
    a = [0]*n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    return a

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join(map(str, a)))

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(' '.join(map(str, A)))

=======
Suggestion 6

def problems280_b():
    return None

=======
Suggestion 7

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    for i in range(N-1):
        A[i] = S[i] + A[i-1]
    A[N-1] = S[N-1] + A[N-2]
    print(' '.join(map(str, A)))
    
solve()
