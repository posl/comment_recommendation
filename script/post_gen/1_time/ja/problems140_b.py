Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i]-1]
        if i < N-1 and A[i]+1 == A[i+1]:
            satisfaction += C[A[i]-1]

    print(satisfaction)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(i) - 1 for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]]
        if i != 0 and a[i] == a[i - 1] + 1:
            ans += c[a[i - 1]]
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i+1 < N and A[i]+1 == A[i+1]:
            ans += C[A[i]-1]

    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i > 0 and A[i] - A[i - 1] == 1:
            satisfaction += C[A[i - 1] - 1]
    print(satisfaction)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i+1]-a[i] == 1:
            satisfaction += c[a[i]-1]

    print(satisfaction)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            ans += c[a[i]-1]

    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    satisfaction = 0
    for i in range(0, N):
        satisfaction += B[A[i] - 1]
        if i < N - 1 and A[i] + 1 == A[i + 1]:
            satisfaction += C[A[i] - 1]
    print(satisfaction)

=======
Suggestion 8

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    return n, a, b, c

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        ans += b[a[i]-1]
        if i != n-1 and a[i+1] == a[i] + 1:
            ans += c[a[i]-1]

    print(ans)

=======
Suggestion 10

def get_score(N, A, B, C):
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i] == A[i+1]-1:
            score += C[A[i]-1]
    return score
