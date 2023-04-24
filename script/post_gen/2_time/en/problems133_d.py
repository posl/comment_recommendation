Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = (A[0] + A[N-1] - A[1]) // 2
    for i in range(1, N):
        ans[i] = A[i-1] - ans[i-1]
    print(" ".join(map(str, ans)))

main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = [0] * n
    x[0] = (a[0] + a[-1] - a[1]) // 2
    for i in range(1, n):
        x[i] = a[i - 1] - x[i - 1]
    print(" ".join(map(str, x)))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        X[i] = (A[i - 1] - A[i]) // 2
    for i in range(N):
        X[i] += X[i - 1]
    for i in range(N):
        X[i] += A[i]
    print(*X)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] - A[(i + 1) % N]
    for i in range(N):
        C[i] = B[(i - 1) % N] + B[i]
    for i in range(N):
        print(C[i] // 2, end=' ')

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    ans[0] = sum(A)
    for i in range(N-1):
        ans[0] -= 2*A[i+1]
    for i in range(N-1):
        ans[i+1] = 2*A[i] - ans[i]
    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) - N * A[1]
    ans[0] //= 2
    for i in range(1, N):
        ans[i] = A[i - 1] - ans[i - 1]
    print(*ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = (A[i-1] - A[i])//2
    print(*B)
    return

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    B[0] = sum(A) // (N-1)
    for i in range(N-1):
        B[i+1] = A[i] - B[i]
    print(*B)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2x liters of rain = x liters of water
    # A_i = x + x + x + x
    # A_i = 4x
    # x = A_i / 4
    # 2x liters of rain = x liters of water
    # 2x = A_i / 4
    # x = A_i / 8
    # A_i = 8x
    # A_i = 8(A_i / 8) = 8(A_i // 8)
    # A_i = 8(A_i // 8) + (A_i % 8)

=======
Suggestion 10

def read():
    return int(input())
