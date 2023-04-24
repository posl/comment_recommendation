Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 19):
        ans += (N // (10 ** i)) * (10 ** (i - 1))
        ans %= MOD
        if N % (10 ** i) >= (10 ** (i - 1)):
            ans += (N % (10 ** i)) - (10 ** (i - 1)) + 1
            ans %= MOD
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**i))*(10**(i-1))
        if N%(10**i) >= 10**(i-1):
            ans += 10**(i-1)
        else:
            ans += N%(10**i)+1
    print(ans%MOD)
    return

=======
Suggestion 3

def main():
    N = int(input())

    ans = 0
    for i in range(1, 19):
        ans += min(10**i-1, N) - 10**(i-1) + 1

    print(ans % 998244353)

=======
Suggestion 4

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 18):
        ans += N // 10 ** i * (10 ** i - 10 ** (i - 1))
        ans %= MOD
        ans += max(N % 10 ** i - 10 ** (i - 1) + 1, 0)
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, 18):
        ans += (N // 10**i) * 9 * 10**(i - 1)
        ans += max(0, N % 10**i - 10**(i - 1) + 1)
    ans %= 998244353
    print(ans)

=======
Suggestion 6

def f(n):
    if n == 0:
        return 0
    if n < 10:
        return n
    k = len(str(n))
    return (n - 10 ** (k - 1) + 1) + 9 * (k - 1) * (10 ** (k - 2))

=======
Suggestion 7

def  main():
    N = int(input())
    ans = 0
    for  i  in  range(1, 10):
        ans += (N - i) // 10 + 1
    print(ans % 998244353)

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1,10):
        ans += sum(i * 10**j for j in range(18)) * (N // (i * 10**18))
        ans += sum(i * 10**j for j in range(N % (i * 10**18) // i + 1)) % MOD
    print(ans % MOD)

=======
Suggestion 9

def main():
    N = int(input())
    MOD = 998244353

    # 1桁の数の総和は 1+2+3+...+9=45
    # 2桁の数の総和は 10+11+12+...+99=900
    # 3桁の数の総和は 100+101+102+...+999=9000
    # 4桁の数の総和は 1000+1001+1002+...+9999=90000
    # 5桁の数の総和は 10000+10001+10002+...+99999=900000
    # 6桁の数の総和は 100000+100001+100002+...+999999=9000000
    # 7桁の数の総和は 1000000+1000001+1000002+...+9999999=90000000
    # 8桁の数の総和は 10000000+10000001+10000002+...+99999999=900000000
    # 9桁の数の総和は 100000000+100000001+100000002+...+999999999=9000000000
    # 10桁の数の総和は 1000000000+1000000001+1000000002+...+9999999999=90000000000
    # 11桁の数の総和は 10000000000+10000000001+10000000002+...+99999999999=900000000000
    # 12桁の数の総和は 100000000000+100000000001+100000000002+...+999999999999=9000000000000
    # 13桁の数の総和は 1000000000000+1000000000001+1000000000002+...+9999999999999=90000000000000
    # 14桁の数の総和は 100000000000
