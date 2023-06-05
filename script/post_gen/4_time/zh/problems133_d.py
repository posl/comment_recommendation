Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 5
    A = [3, 8, 7, 5, 5]
    # N = 3
    # A = [1000000000, 1000000000, 0]
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    B[0] //= 2
    for i in range(N - 1):
        B[i + 1] = A[i] - B[i]
    for i in range(N):
        print(B[i], end=' ')

=======
Suggestion 2

def solve(n, a):
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    b[0] //= 2
    for i in range(1, n):
        b[i] = a[i-1] - b[i-1]
    for i in range(n):
        b[i] *= 2
    return b

=======
Suggestion 3

def solve(n, a):
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] * 2
    for i in range(n):
        ans[i] -= ans[(i + 1) % n] + ans[(i - 1) % n]
    return ans

=======
Suggestion 4

def test():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        if i == 0:
            B[i] = A[i] - sum(B)
        else:
            B[i] = A[i] - B[i-1]
    print(" ".join(map(str, B)))

=======
Suggestion 5

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (a[i]//2)*2
    for i in range(n):
        if b[i] == 0:
            if i == 0:
                b[n-1] += a[i]//2
                b[i+1] += a[i]//2
            elif i == n-1:
                b[i-1] += a[i]//2
                b[0] += a[i]//2
            else:
                b[i-1] += a[i]//2
                b[i+1] += a[i]//2
    return b

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - A[i - 1]
    print(*B)

=======
Suggestion 7

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - a[(i + 1) % n] // 2
    return b

=======
Suggestion 8

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0 for i in range(N)]
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = 2 * A[i - 1] - B[i - 1]
    print(' '.join([str(i) for i in B]))

=======
Suggestion 9

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = [0] * n
    for i in range(1, n, 2):
        b_list[0] += a_list[i]
    for i in range(1, n):
        b_list[i] = a_list[i - 1] * 2 - b_list[i - 1]
    print(' '.join(map(str, b_list)))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]
    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    print(*ans)
