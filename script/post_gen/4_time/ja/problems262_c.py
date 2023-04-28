Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[A[i]] = i
    ans = 0
    for i in range(1, N + 1):
        if B[i] == i:
            if i + 1 <= N and B[i + 1] == i + 1:
                ans += 1
        else:
            if i < B[i] and B[i] < B[i + 1]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[a[i] - 1] = i + 1
    ans = 0
    for i in range(N):
        if b[i] == i + 1:
            continue
        else:
            ans += 1
            b[a[i] - 1] = b[i]
            a[b[i] - 1] = a[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if min(A[i],A[j]) == i+1 and max(A[i],A[j]) == j+1:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > i + 1:
            continue
        ans += a.count(i + 1)
    print(ans)
main()

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= i+1:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        if i < A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(1, N+1):
        if a[a[i]] == i:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if a[i] > i+1:
            continue
        for j in range(i+1, N):
            if a[i] == i+1 and a[j] == j+1:
                ans += 1
            elif a[i] == j+1 and a[j] == i+1:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= i+1:
            ans += A[i] - (i+1)
        else:
            ans += A[i]

    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if A[i] < i+1:
            continue
        for j in range(A[i], n+1):
            if j < A[j-1]:
                continue
            if A[i] == j and A[j-1] == i+1:
                ans += 1
            if j < A[i]:
                ans += 1
    print(ans)
