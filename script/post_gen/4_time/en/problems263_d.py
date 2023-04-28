Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().sp

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [L if a < L else R if a > R else a for a in A]
    print(sum(A))

=======
Suggestion 3

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(N-1):
        ans += min(2*R, 2*L)
    ans += min(2*R, 2*L)
    print(ans)

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] > 0:
            ans += (a[i+1] - a[i]) * l
        else:
            ans += (a[i+1] - a[i]) * r
    print(ans)

=======
Suggestion 5

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[float('inf')] * 3 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(3):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + a[i]*l)
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a[i]*r)
    print(dp[n][2])

=======
Suggestion 6

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N-1):
        if A[i+1] < A[i]:
            ans += (A[i] - A[i+1]) * L
        else:
            ans += (A[i+1] - A[i]) * R

    print(ans)

=======
Suggestion 7

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(r, l)
        if l <= r:
            r -= l
        else:
            l -= r
    ans += a[-1] + min(l, r)
    print(ans)

=======
Suggestion 8

def calc_min_sum(N, L, R, A):
    min_sum = 0
    for a in A:
        if a < 0:
            min_sum += L * a
        else:
            min_sum += R * a
    return min_sum

=======
Suggestion 9

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)

    #print(N, L, R, A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=", L, "R=", R, "A=", A)

    #print("N=", N, "L=", L, "R=", R, "A=", A)
    #print("N=", N, "L=",

=======
Suggestion 10

def solve(N, L, R, A):
    #print("N, L, R, A", N, L, R, A)
    #print("A", A)
    #print("A[0:N//2]", A[0:N//2])
    #print("A[N//2:N]", A[N//2:N])
    #print("A[N//2:N][::-1]", A[N//2:N][::-1])
    if N == 1:
        if L > 0:
            return L + A[0]
        else:
            return A[0]
    else:
        if L > 0:
            if N % 2 == 0:
                return L + sum(A[0:N//2]) + R + sum(A[N//2:N][::-1])
            else:
                return L + sum(A[0:N//2]) + R + sum(A[N//2:N][::-1]) + A[N//2]
        else:
            if N % 2 == 0:
                return sum(A[0:N//2]) + R + sum(A[N//2:N][::-1])
            else:
                return sum(A[0:N//2]) + R + sum(A[N//2:N][::-1]) + A[N//2]
