Synthesizing 10/10 solutions

=======
Suggestion 1

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
        ans += (2 ** i) * zero * one
    print(ans % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1<<i):
                cnt += 1
        ans += (cnt*(N-cnt)*(1<<i))
    print(ans%1000000007)

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (1 << i) * cnt * (n - cnt)
        ans %= mod
    print(ans)

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for j in range(n):
            if a[j] >> i & 1:
                c += 1
        ans += c * (n - c) * pow(2, i, 10**9+7)
        ans %= 10**9+7
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & 1:
                cnt += 1
            A[j] >>= 1
        ans += cnt * (N - cnt) * (1 << i)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for a in A:
            if (a >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += (zero * one) * (2**i)
        ans %= MOD

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    mod = 10**9+7
    for i in range(60):
        zero = 0
        one = 0
        for j in range(n):
            if a[j]>>i & 1:
                one += 1
            else:
                zero += 1
        ans += (zero*one)%mod * pow(2,i,mod)%mod
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        zero = 0
        for j in range(n):
            if (a[j] >> i) & 1 == 0:
                zero += 1
        ans += zero * (n - zero) * (1 << i)
        ans %= 10 ** 9 + 7
    print(ans)
solve()

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    ans = 0
    for i in range(60):
        #iビット目が立っている数を数える
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        #iビット目が立っている数がcnt個あるとき、iビット目に1を立てたときのXORの回数はcnt*(N-cnt)
        #例えばiビット目に1を立てたときのXORの回数は、iビット目が0のときの数と同じになる
        #iビット目が1のときの数は、iビット目が0のときの数とXORを取ったときにiビット目が1になる
        #iビット目が1のときの数は、iビット目が1のときの数とXORを取ったときにiビット目が0になる
        #よって、iビット目が1のときの数は、iビット目が0のときの数と同じになる
        ans += cnt * (N - cnt) * pow(2, i, MOD)
        ans %= MOD
    print(ans)

solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #全てのXORを求める
    xor_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            xor_sum += A[i] ^ A[j]

    print(xor_sum % (10**9+7))
