Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        x = 0
        for j in range(n):
            if (a[j]>>i)&1:
                x += 1
        ans += ((1<<i)%mod) * (x*(n-x)%mod)
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (n - cnt) * pow(2, i, mod))
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #print(2**60)
    #print(2**60-1)
    #print(2**60-1 < 2**60)
    #print(2**60-1 < 2**60-1)
    #print(2**60-1 < 2**60-2)
    #print(2**60-1 < 2**60-3)
    #print(2**60-1 < 2**60-4)
    #print(2**60-1 < 2**60-5)
    #print(2**60-1 < 2**60-6)
    #print(2**60-1 < 2**60-7)
    #print(2**60-1 < 2**60-8)
    #print(2**60-1 < 2**60-9)
    #print(2**60-1 < 2**60-10)
    #print(2**60-1 < 2**60-11)
    #print(2**60-1 < 2**60-12)
    #print(2**60-1 < 2**60-13)
    #print(2**60-1 < 2**60-14)
    #print(2**60-1 < 2**60-15)
    #print(2**60-1 < 2**60-16)
    #print(2**60-1 < 2**60-17)
    #print(2**60-1 < 2**60-18)
    #print(2**60-1 < 2**60-19)
    #print(2**60-1 < 2**60-20)
    #print(2**60-1 < 2**60-21)
    #print(2**60-1 < 2**60-22)
    #print(2**60-1 < 2**60-23)
    #print(2**60-1 < 2**60-24)
    #print(2**60-1 < 2**60-25)
    #print(2**60-1 < 2**60-26

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(n):
            if a[j] & (1 << i):
                one += 1
            else:
                zero += 1
        ans += (zero * one) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 6

def solve():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for i in range(60):
        # 计算第i位的答案
        # 令c0为第i位为0的A的个数，c1为第i位为1的A的个数
        c0 = 0
        c1 = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                c1 += 1
            else:
                c0 += 1
        # 第i位的答案为c0 * c1 * 2^i
        ans += c0 * c1 * (1 << i)
        ans %= 10**9 + 7

    # 打印答案
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7

    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1<<i):
                cnt += 1
        ans += (cnt*(n-cnt)*(1<<i))
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().strip().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a & (1 << i):
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 9

def calXor(a,b):
    c = a^b
    return c

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        num = 0
        for j in range(N):
            if A[j] & (1 << i):
                num += 1
        ans += num * (N - num) * (1 << i)
        ans %= mod
    print(ans)
