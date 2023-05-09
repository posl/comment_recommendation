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
        ans += cnt * (N - cnt) * (1 << i)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * pow(2, i, mod)) % mod
        ans %= mod
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= 10**9+7
    print(ans)
solve()

=======
Suggestion 4

def xor_sum(n, a):
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i))
        ans %= 1000000007
    return ans

n = int(input())
a = list(map(int, input().split()))
print(xor_sum(n, a))

=======
Suggestion 5

def solve():
    # write your code here
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        count = 0
        for j in range(N):
            if A[j] & (1 << i):
                count += 1
        ans += (count * (N - count) * (1 << i)) % MOD
    print(ans % MOD)

=======
Suggestion 6

def solve(N, A):
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1 << i):
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
        ans %= mod
    return ans

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    result = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(N):
            if A[j] & 1:
                one += 1
            else:
                zero += 1
            A[j] >>= 1
        result += (one * zero * (1 << i)) % MOD
    print(result % MOD)

=======
Suggestion 8

def xor_sum(a):
    sum = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            sum += a[i] ^ a[j]
    return sum

=======
Suggestion 9

def xor_sum(a):
    res = 0
    for i in range(60):
        cnt = 0
        for j in range(len(a)):
            if(a[j] >> i) & 1:
                cnt += 1
        res += (cnt*(len(a)-cnt)) * (1 << i)
        res %= 10**9+7
    return res

N = int(input())
A = list(map(int, input().split()))
print(xor_sum(A))

=======
Suggestion 10

def solve():
    from collections import Counter
    from itertools import accumulate
    MOD = 10**9+7
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    C = [v*(N-v) for v in C.values()]
    C = list(accumulate(C))
    ans = 0
    for c in C[:-1]:
        ans += c
        ans %= MOD
    print(ans)
