Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
    ans = 0
    for i in range(N-1):
        if B[i] < 0:
            ans += abs(B[i])
            B[i] = 0
    if B[N-1] < 0:
        ans += abs(B[N-1])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(N - 1):
        B[i + 1] = A[i + 1] + B[i]
    B = [abs(b) for b in B]
    print(sum(B))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    B[0] = A[0]
    B[n-1] = A[n-1]
    for i in range(1, n-1):
        B[i] = A[i] + A[i-1]
    B.sort()
    print(sum(B))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    ans = 0
    for i in range(N):
        if i%2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    ans = sum(B)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    if N == 2:
        print(ans)
        return
    for i in range(N-2):
        ans += abs(A[i] - A[i+1])
    ans += abs(A[N-2])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = A[:]
    for i in range(N - 1):
        B[i + 1] = A[i] + A[i + 1]
    ans = 0
    for i in range(N):
        ans += B[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    if N%2 == 0:
        B = [abs(A[i]) for i in range(N) if i%2 == 1]
        ans -= 2*min(B)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1回目の操作
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    ans = sum(B)

    # 2回目の操作
    for i in range(N):
        if i % 2 == 0:
            B[i] = -A[i]
        else:
            B[i] = A[i]
    ans = max(ans, sum(B))

    print(ans)
