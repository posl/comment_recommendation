Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = sum(A)
    for i in range(1, N):
        B[i] = A[i-1] - B[i-1] // 2
    print(*B)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = (A[i] + A[i+1]) // 2
        elif i == N - 1:
            ans[i] = (A[i] + A[0]) // 2
        else:
            ans[i] = (A[i] + A[i+1]) // 2
    for i in range(N):
        print(ans[i], end = " ")
    print()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N

    ans[0] = sum(A) - 2 * sum(A[1::2])
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]

    print(*ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] + A[(i + 1) % N]
    print(*B)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] - A[(i+1)%N]
    C = [0 for i in range(N)]
    for i in range(N):
        C[i] = (B[i] + B[(i-1)%N])//2
    print(*C)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x ^= a[i]
    print(x, end="")
    for i in range(n-1):
        x ^= a[i]
        print(" " + str(x), end="")
    print()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(a[i] + a[(i+1)%n])
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(0)
    ans[0] = sum(A) - N * A[1]
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    for i in range(N):
        print(ans[i], end=" ")
    print()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    ans = [0] * n

    ans[0] = s
    for i in range(n - 1):
        ans[i + 1] = a[i] - ans[i] // 2

    print(*ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(A[0])
    if N == 3:
        print(A[0]+A[1]-A[2], A[1]+A[2]-A[3], A[2]+A[3]-A[0])
    else:
        B = [0]*N
        for i in range(N):
            B[i] = (A[i]+A[i+1])//2
        print(*B)

main()
