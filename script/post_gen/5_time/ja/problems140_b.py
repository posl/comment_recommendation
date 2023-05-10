Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i]-1]
        if i != N-1 and A[i]+1 == A[i+1]:
            satisfaction += C[A[i]-1]
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
        if i != n-1 and a[i+1]-a[i] == 1:
            satisfaction += c[a[i]-1]

    print(satisfaction)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i != n-1 and a[i]+1 == a[i+1]:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    satisfaction += B[A[0]-1]
    for i in range(N-1):
        satisfaction += B[A[i+1]-1]
        if A[i+1] - A[i] == 1:
            satisfaction += C[A[i]-1]

    print(satisfaction)

=======
Suggestion 5

def get_ints(): return map(int, input().split())

n = int(input())
a = list(get_ints())
b = list(get_ints())
c = list(get_ints())

ans = 0
for i in range(n):
    ans += b[a[i]-1]
    if i < n - 1 and a[i] == a[i+1] - 1:
        ans += c[a[i]-1]

print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i != 0 and a[i] == a[i-1]+1:
            satisfaction += c[a[i-1]-1]
    print(satisfaction)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i]-1]
        if i < N-1 and A[i+1] - A[i] == 1:
            satisfaction += C[A[i]-1]
    print(satisfaction)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i != n-1 and a[i] == a[i+1]-1:
            ans += c[a[i]-1]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i]-1]
        if i != N-1 and A[i+1]-A[i] == 1:
            satisfaction += C[A[i]-1]
    print(satisfaction)
