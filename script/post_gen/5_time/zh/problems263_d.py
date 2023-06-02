Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, L, R)
    # print(A)
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
    # print(A)
    sumA = sum(A)
    # print(sumA)
    for i in range(N):
        if A[i] < L:
            sumA += (L - A[i])
            A[i] = L
    # print(A)
    for i in range(N):
        if A[i] > R:
            sumA += (A[i] - R)
            A[i] = R
    # print(A)
    print(sumA)

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < 0:
            ans += -A[i] * L
        else:
            ans += A[i] * R
    print(ans)

=======
Suggestion 3

def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if l > 0:
        if r > 0:
            print(sum(a) - (a[0] + a[1] - l - r) * 2)
        else:
            print(sum(a) - (a[0] - l) * 2)
    else:
        if r > 0:
            print(sum(a) - (a[1] - r) * 2)
        else:
            print(sum(a))

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    min_sum = sum(a[:n - l + 1])
    max_sum = sum(a[-r:])
    print(max_sum - min_sum)

=======
Suggestion 5

def solve(N, L, R, A):
    # print(N, L, R, A)
    # print('A', A)
    # print('L', L)
    # print('R', R)
    # print('L + R', L + R)
    # print('A + L + R', A + L + R)
    # print('min(A + L + R)', min(A + L + R))
    return sum(A) + min(A + L + R) * (N - 2)

=======
Suggestion 6

def minsum(N, L, R, A):
    ans = 0
    for i in range(N):
        if A[i] > 0:
            ans += A[i] * R
        else:
            ans += A[i] * L
    return ans

=======
Suggestion 7

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        a[i] += l
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i)
    for i in range(n):
        a[i] += r - l
    for i in range(n):
        ans = min(ans, a[i] * (n - i) + sum(a[i + 1:]))
    print(ans)

=======
Suggestion 8

def solve():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    #print(A)
    #print(N,L,R)
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0],A[1],A[2],A[3],A[4])
    #print(A[N-1],A[N-2],A[N-3],A[N-4],A[N-5])
    #print(A[0

=======
Suggestion 9

def solve(n, l, r, a):
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = min(dp[i - 1][0] + l * a[i - 1], dp[i - 1][1] + l * a[i - 1])
        dp[i][1] = min(dp[i - 1][0] + r * a[i - 1], dp[i - 1][1] + r * a[i - 1])
    return min(dp[n][0], dp[n][1])

=======
Suggestion 10

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    if L < 0 and R < 0:
        for i in range(N):
            if A[i] < 0:
                ans += -L * A[i]
            else:
                ans += -R * A[i]
    elif L < 0 and R >= 0:
        for i in range(N):
            if A[i] < 0:
                ans += -L * A[i]
            else:
                ans += R * A[i]
    elif L >= 0 and R < 0:
        for i in range(N):
            if A[i] < 0:
                ans += L * A[i]
            else:
                ans += -R * A[i]
    else:
        for i in range(N):
            if A[i] < 0:
                ans += L * A[i]
            else:
                ans += R * A[i]
    print(ans)
