Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += ((1 << i) * cnt * (n - cnt)) % (10 ** 9 + 7)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if (a >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * pow(2, i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * pow(2, i, MOD)) % MOD
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += zero * one * (2 ** i)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if a & (1 << i):
                c += 1
        ans += c * (N - c) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        cnt0 = 0
        cnt1 = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt1 += 1
            else:
                cnt0 += 1
        ans += (cnt0 * cnt1) * (2 ** i)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if (a >> i) & 1:
                c += 1
        ans += (1 << i) * c * (N - c)
        ans %= 10 ** 9 + 7
    print(ans)

solve()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        x = 0
        for j in range(n):
            if a[j]>>i & 1:
                x += 1
        ans += x*(n-x)*pow(2,i,mod)
        ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if ((a[j] >> i) & 1):
                cnt += 1
        ans += (cnt * (n - cnt) * pow(2, i, 10 ** 9 + 7)) % (10 ** 9 + 7)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 10

def main():
    import sys
    import math
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        count = 0
        for a in A:
            if a>>i&1:
                count += 1
        ans += (1<<i) * count * (N-count)
        ans %= mod
    print(ans)
