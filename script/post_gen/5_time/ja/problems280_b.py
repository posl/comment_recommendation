Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(N-1):
        A[i+1] = S[i+1] - A[i]
    print(*A, sep=" ")

=======
Suggestion 2

def problem280_b():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        a[i] = s[i] - sum(a[:i])
    print(*a)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(' '.join(map(str, A)))

=======
Suggestion 4

def solve():
    N = int(input())
    S = list(map(int,input().split()))
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(1,N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(*a)

=======
Suggestion 6

def main():
    N=int(input())
    S=list(map(int,input().split()))
    A=[0]*N
    A[0]=S[0]
    for i in range(1,N):
        A[i]=S[i]-S[i-1]
    print(*A)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1,N):
        A[i] = S[i] - S[i-1]
    print(" ".join(map(str, A)))

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(n-1):
        a[i+1] = s[i+1] - a[i]
    print(*a)

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    print(' '.join(map(str, A)))
