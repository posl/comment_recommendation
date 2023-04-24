Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][1 << i | 1 << j] = A[i][j]

    for i in range(1, 1 << N):
        for j in range(N):
            if not (i >> j & 1):
                continue
            for k in range(N):
                if i >> k & 1:
                    continue
                dp[k + 1][i | 1 << k] = max(dp[k + 1][i | 1 << k], dp[j + 1][i] + A[j][k])

    print(dp[N][(1 << N) - 1])

solve()

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    dp = [[0 for _ in range(2**N)] for _ in range(N+1)]
    for i in range(N):
        for j in range(2**i):
            for k in range(2**(N-i-1)):
                dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j] ^ A[i][j+k])

    print(dp[N][2**N-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    dp = [[0] * (1 << N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i < j:
                dp[i][1 << i | 1 << j] = A[i][j]

    for i in range(1 << N):
        for j in range(N):
            if i & 1 << j:
                for k in range(N):
                    if i & 1 << k:
                        dp[k][i] = max(dp[k][i], dp[k][i ^ 1 << j] + A[k][j])

    print(dp[N - 1][(1 << N) - 1])

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for i in range(2**N)] for j in range(N)]
    for i in range(N):
        for j in range(2**N):
            for k in range(N):
                if j & (1 << k) == 0:
                    dp[i][j | (1 << k)] = max(dp[i][j | (1 << k)], dp[i][j] ^ A[i][k])
    ans = 0
    for i in range(2**N):
        ans = max(ans, dp[N-1][i])
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for _ in range(1 << N)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(i + 1, N):
            dp[2][1 << i | 1 << j] = A[i][j]
    for i in range(3, N + 1):
        for bit in range(1 << N):
            if bin(bit).count('1') != i:
                continue
            for j in range(N):
                if not bit & 1 << j:
                    continue
                for k in range(j + 1, N):
                    if not bit & 1 << k:
                        continue
                    dp[i][bit] = max(dp[i][bit], dp[i - 1][bit ^ 1 << j ^ 1 << k] + A[j][k])
    print(dp[N][(1 << N) - 1])

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1 << N):
        bit = bin(i)[2:].zfill(N)
        pair = []
        for j in range(N):
            if bit[j] == '1':
                pair.append(j)
        if len(pair) == 2:
            ans = max(ans, A[pair[0]][pair[1]])
        elif len(pair) > 2:
            for j in range(len(pair)):
                for k in range(j + 1, len(pair)):
                    ans = max(ans, A[pair[j]][pair[k]])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for _ in range(2 ** N)] for _ in range(N)]
    for i in range(N):
        for j in range(2 ** N):
            for k in range(N):
                if (j & (1 << k)) == 0:
                    dp[i][j | (1 << k)] = max(dp[i][j | (1 << k)], dp[i][j] ^ A[i][k])
    dp2 = [0 for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(N):
            if (i & (1 << j)) == 0:
                dp2[i | (1 << j)] = max(dp2[i | (1 << j)], dp[j][i])
    print(dp2[2 ** N - 1])

=======
Suggestion 8

def f(a):
    if len(a) == 1:
        return a[0]
    else:
        return max([a[0]^a[i] + f(a[1:i]+a[i+1:]) for i in range(1,len(a))])

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

print(f([a[i][j] for i in range(n) for j in range(i+1,n)]))

=======
Suggestion 9

def calc_xor(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] ^ calc_xor(lst[1:])


N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

=======
Suggestion 10

def f(x, y):
    if x > y:
        return f(y, x)
    if y % x == 0:
        return x
    return f(y % x, x)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dp[i + 1][1 << i | 1 << j] = f(a[i][j], a[i][j])

for i in range(n):
    for j in range(1 << n):
        if not (j >> i & 1):
            continue
        for k in range(n):
            if i == k:
                continue
            if j >> k & 1:
                continue
            dp[k + 1][j | 1 << k] = max(dp[k + 1][j | 1 << k], dp[i + 1][j] ^ a[i][k])

print(dp[n][(1 << n) - 1])
