Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for j in range(n):
            if a[j] & (1 << i):
                c += 1
        ans += c * (n - c) * (1 << i)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * pow(2, i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1<<i):
                cnt += 1
        ans += cnt * (N - cnt) * (1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        one = 0
        zero = 0
        for a in A:
            if (a >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += one * zero * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if (a >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if a & (1 << i):
                c += 1
        ans += (c * (N - c) * (1 << i)) % MOD
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        c0 = 0
        c1 = 0
        for a in A:
            if a & (1 << i) == 0:
                c0 += 1
            else:
                c1 += 1
        ans += (1 << i) * c0 * c1 % mod
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    *A, = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(61):
        cnt = 0
        for a in A:
            if a & (1 << i):
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
        ans %= MOD
    print(ans)

=======
Suggestion 9

def solve(n, A):
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a & (1<<i):
                cnt += 1
        ans += (1<<i) * cnt * (n-cnt)
        ans %= MOD
    return ans

n = int(input())
A = list(map(int, input().split()))
print(solve(n, A))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    # A[i]の下位60bitの各bitについて、そのbitが立っている数を数える
    # その数がbitが立っている数を数える
    # その数がbitが立っている数を数える
    bit_count = [0] * 60
    for a in A:
        for i in range(60):
            if a >> i & 1:
                bit_count[i] += 1

    # bit_count[i]が立っている数を数える
    # その数がbitが立っている数を数える
    # その数がbitが立っている数を数える
    ans = 0
    for i in range(60):
        ans += (1 << i) * bit_count[i] * (N - bit_count[i])
        ans %= MOD
    print(ans)
