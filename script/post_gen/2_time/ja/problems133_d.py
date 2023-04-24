Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = sum(A)
    for i in range(1, N):
        B[i] = A[i - 1] - B[i - 1] // 2
    B = list(map(str, B))
    print(" ".join(B))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A)
    for i in range(N-1):
        ans[i+1] = A[i] * 2 - ans[i]
    print(*ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0] * N
    ans[0] = sum(A) - 2 * sum(A[1::2])
    for i in range(1,N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    print(*ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A[1::2]) - sum(A[0::2])
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    print(*ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) - (N - 2) * A[0]
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = [0]*N
    ans[0] = sum(A)
    for i in range(1,N):
        ans[i] = 2*A[i-1]-ans[i-1]

    print(*ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - A[i-1]
    B = B[1:] + B[:1]
    C = [0 for _ in range(N)]
    for i in range(N):
        C[i] = (B[i] + B[i-1])//2
    print(*C)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    for i in range(N):
        ans[i] = ((A[i-1] + A[i])//2)
    print(*ans)
