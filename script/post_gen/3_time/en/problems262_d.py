Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, mod) * (N - i) * A[i]
        ans %= mod
    print(ans)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    mod = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += pow(2, i, mod) * pow(2, N-1-i, mod) * A[i]
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        for j in range(2**N):
            if bin(j).count("1") == i:
                tmp = 0
                for k in range(N):
                    if (j >> k) & 1:
                        tmp += A[k]
                if tmp % i == 0:
                    ans += 1
    print(ans % MOD)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    mod = 998244353
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt += 1
                sum += A[j]
        if sum % cnt == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1,N+1):
        ans += pow(2,N-i,MOD)*i*pow(2,i-1,MOD)*sum(A[i-1::i])
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += pow(2, i, 998244353) * (N - i) * A[i]
        ans %= 998244353
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(1, 2**N):
        S = 0
        for j in range(N):
            if i >> j & 1:
                S += A[j]
        if S % bin(i).count('1') == 0:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for bit in range(1 << n):
        count = 0
        sum = 0
        for i in range(n):
            if bit & (1 << i):
                count += 1
                sum += a[i]
        if sum % count == 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def input():
    return sys.stdin.readline()[:-1]
