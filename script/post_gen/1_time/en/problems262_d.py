Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, MOD) * (pow(2, N - i - 1, MOD) - 1) * A[i]
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2,i,mod)*pow(2,N-i-1,mod)*A[i]
        ans %= mod
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        sum = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
                sum += A[j]
        if sum % cnt == 0:
            ans += 1
    print(ans % MOD)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i >> j & 1:
                s += A[j]
        if s % bin(i).count('1') == 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 2**N):
        count = 0
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                count += 1
                sum += A[j]
        if sum % count == 0:
            ans += 1
    print(ans % MOD)

=======
Suggestion 6

def main():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)]
    dp[0] = 1
    for i in range(N):
        for j in range(N - 1, -1, -1):
            dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
    ans = 0
    for i in range(1, N + 1):
        ans += (dp[i] * A[i - 1] * pow(i, MOD - 2, MOD)) % MOD
    print(ans % MOD)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1,2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
        if s % bin(i).count('1') == 0:
            ans += 1
    print(ans % MOD)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    ans = 0
    for bit in range(1, 1 << N):
        prod = 1
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                prod *= A[i]
                cnt += 1
        if prod % cnt == 0:
            ans += 1
    print(ans % MOD)

=======
Suggestion 9

def main():
    def solve():
        mod = 998244353
        N = int(input())
        A = list(map(int, input().split()))
        ans = pow(2, N, mod) - 1
        for i in range(N):
            ans = (ans - pow(2, i, mod) * pow(2, N - i - 1, mod) * (N - i) * A[i]) % mod
        print(ans)
    solve()

=======
Suggestion 10

def count_int_averages(A):
    N = len(A)
    mod = 998244353
    ans = 0
    for i in range(1, 2 ** N):
        bits = bin(i)[2:].zfill(N)
        cnt = sum([int(b) for b in bits])
        s = sum([int(bits[j]) * A[j] for j in range(N)])
        if s % cnt == 0:
            ans += 1
    return ans % mod
