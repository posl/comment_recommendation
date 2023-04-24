Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1 << i):
                cnt += 1
        ans += (1 << i) * cnt * (N - cnt)
        ans %= 1000000007
    print(ans)

=======
Suggestion 2

def main():
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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt0 = 0
        cnt1 = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt1 += 1
            else:
                cnt0 += 1
        ans += cnt0 * cnt1 * (2 ** i)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i] ^ A[j]
    print(sum % (10**9 + 7))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        a = 0
        b = 0
        for j in range(N):
            if ((A[j] >> i) & 1) == 1:
                a += 1
            else:
                b += 1
        ans += (a * b) * (2 ** i)
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        a = 0
        b = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                a += 1
            else:
                b += 1
        ans += a * b * pow(2, i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        res += cnt * (n - cnt) * pow(2, i, 10**9+7)
        res %= 10**9+7
    print(res)

=======
Suggestion 8

def main():
    n = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (A[j] >> i) & 1:
                cnt += 1
        ans = (ans + cnt * (n - cnt) * pow(2, i, MOD)) % MOD
    print(ans)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    As = list(map(int, input().split()))
    mo = 10**9+7

    #compute
    ans = 0
    for i in range(60):
        cnt = 0
        for A in As:
            if A >> i & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * (2**i)) % mo

    #output
    print(ans % mo)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)

    # 0 から 60 までの桁の合計を計算
    sum = [0] * 60
    for a in A:
        for i in range(60):
            sum[i] += (a >> i) & 1

    #print(sum)

    # 60 までの桁の合計を 2 で割った余りを計算
    # 2 で割った余りが 0 の場合は、同じ桁のビットが偶数個
    # 2 で割った余りが 1 の場合は、同じ桁のビットが奇数個
    # 2 で割った余りが 1 の場合は、同じ桁のビットが奇数個
    # 同じ桁のビットが奇数個の場合、ビットごとの排他的論理和は 1 になる
    # 同じ桁のビットが偶数個の場合、ビットごとの排他的論理和は 0 になる
    # 同じ桁のビットが偶数個の場合、ビットごとの排他的論理和は 0 になる
    # 60 までの桁の合計を 2 で割った余りが 1 の場合は、ビットごとの排他的論理和が 1 になる
    # 60 までの桁の合計を 2 で割った余りが 1 の場合は、ビットごとの排他的論理和が 1 になる
    # 60 までの桁の合計を 2 で割った余りが 1 の場合は、ビットごとの排他的論理和が 1 にな
