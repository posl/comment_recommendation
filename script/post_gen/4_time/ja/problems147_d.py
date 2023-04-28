Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j]>>i&1:
                cnt += 1
        ans += (cnt*(n-cnt)%mod)*(1<<i)%mod
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & 1:
                cnt += 1
            a[j] >>= 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 3

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
        ans += (cnt * (N-cnt) * (1<<i))
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        count = 0
        for j in range(N):
            if A[j] & 1:
                count += 1
            A[j] >>= 1
        ans += count*(N-count)*pow(2,i,MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += 2**(i+1) * cnt * (n-cnt)
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a & 1:
                cnt += 1
            a >>= 1
        ans += cnt * (N - cnt) * (2 ** i)
        ans %= mod
    print(ans)
main()

=======
Suggestion 7

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 3
    a = [1, 2, 3]
    # n = 10
    # a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # n = 10
    # a = [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]
    # n = 300000
    # a = [1] * 300000
    # print(a)
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        one = 0
        for j in range(n):
            if a[j] & (1 << i):
                one += 1
        ans += (one * (n - one) * (1 << i))
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        bit = 0
        for j in range(n):
            if a[j] >> i & 1:
                bit += 1
        ans += bit * (n - bit) * pow(2, i, mod)
        ans %= mod
    print(ans)

solve()

=======
Suggestion 9

def xor_sum(n, a):
    ans = 0
    for i in range(60):
        count = 0
        for j in range(n):
            if a[j] & (1 << i):
                count += 1
        ans += (count * (n - count) * (1 << i)) % (10**9+7)
    return ans % (10**9+7)

n = int(input())
a = list(map(int, input().split()))
print(xor_sum(n, a))

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7

    #ビットごとに1が立っている数
    bit_count = [0] * 60
    for a in A:
        for bit in range(60):
            if a & (1<<bit):
                bit_count[bit] += 1

    #ビットごとに1が立っている数の組み合わせ
    bit_comb = [0] * 60
    for bit in range(60):
        bit_comb[bit] = bit_count[bit] * (N - bit_count[bit])

    #ビットごとに1が立っている数の組み合わせの和
    bit_sum = 0
    for bit in range(60):
        bit_sum += bit_comb[bit] * (1<<bit)

    print(bit_sum % mod)
