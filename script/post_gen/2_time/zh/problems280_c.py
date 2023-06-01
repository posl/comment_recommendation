Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]
    print(*a)

main()

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join(map(str, a)))

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i - 1]
    print(*A)

=======
Suggestion 4

def solve(N, S):
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[0]
    return A

=======
Suggestion 5

def main():
    n = input()
    s = raw_input().split()
    s = [int(x) for x in s]
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - a[i-1]
    print ' '.join(map(str, a))

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(" ".join(map(str, a)))

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 8

def solve():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    for i in range(n-1):
        a[i] = s[i] + a[i-1]
    a[n-1] = s[n-1] + a[n-2]
    print(' '.join(map(str, a)))

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0]*N
    A[0] = S[0]
    for i in range(N-1):
        A[i+1] = S[i+1] - S[i]
    print(' '.join(map(str, A)))
