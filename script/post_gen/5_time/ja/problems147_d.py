Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        one = 0
        zero = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += (one * zero * pow(2, i, 10**9+7))
        ans %= 10**9+7
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * pow(2, i, 10**9 + 7)) % (10**9 + 7)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        o = 0
        for a in A:
            if a>>i&1:
                o += 1
        ans += o*(N-o)*2**i
        ans %= MOD
    print(ans)

=======
Suggestion 4

def xor(x, y):
    return x ^ y

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        bit = 0
        for j in range(n):
            if a[j]&(1<<i):
                bit += 1
        ans += bit*(n-bit)*(1<<i)
        ans %= 10**9+7
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    #print(n)
    #print(a_list)
    sum_list = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum_list.append(a_list[i] ^ a_list[j])
    #print(sum_list)
    print(sum(sum_list) % (10**9+7))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1<<i):
                cnt += 1
        ans += (cnt * (N-cnt) * (1<<i))
        ans %= MOD
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        x = 0
        for j in range(n):
            if a[j] & (1 << i):
                x += 1
        ans += (x * (n - x) * (1 << i))
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        mask = 1 << i
        count = 0
        for a in A:
            if a & mask:
                count += 1
        ans += (count * (N-count) * mask)
        ans %= (10**9+7)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i)) % (10**9 + 7)
        ans %= (10**9 + 7)
    print(ans)
