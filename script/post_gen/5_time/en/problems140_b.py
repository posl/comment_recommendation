Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i > 0 and A[i - 1] + 1 == A[i]:
            satisfaction += C[A[i - 1] - 1]

    print(satisfaction)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i > 0 and a[i] - a[i-1] == 1:
            satisfaction += c[a[i-1]-1]

    print(satisfaction)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i > 0 and a[i] == a[i-1] + 1:
            satisfaction += c[a[i-1]-1]

    print(satisfaction)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i < N-1 and A[i]+1 == A[i+1]:
            ans += C[A[i]-1]
    
    print(ans)

=======
Suggestion 5

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, A, B, C

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i]-1]
        if i != N-1:
            if A[i]+1 == A[i+1]:
                satisfaction += C[A[i]-1]
    print(satisfaction)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i > 0 and a[i-1] + 1 == a[i]:
            total += c[a[i-1]-1]

    print(total)

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

def solve(N, A, B, C):
    satisfaction = 0
    for i in range(0, N):
        satisfaction += B[A[i]-1]
        if i < N-1 and A[i+1] == A[i] + 1:
            satisfaction += C[A[i]-1]
    return satisfaction

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

print(solve(N, A, B, C))
