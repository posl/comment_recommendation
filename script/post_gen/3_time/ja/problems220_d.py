Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        cnt = 0
        for a in A:
            if a == i:
                cnt += 1
        ans[i] = pow(2, cnt - 1, mod)
    print(*ans, sep='

')

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # 0 以上 9 以下の整数からなる長さ N の数列 A=(A_1,...,A_N) があり、この順に左から右に並んでいます。
    # 数列の長さが 1 になるまで、操作 F または操作 G を繰り返し行います。
    # 操作 F ：左端の 2 つの値 ( x,y とする ) を削除した後、一番左に (x+y)%10 を挿入する
    # 操作 G ：左端の 2 つの値 ( x,y とする ) を削除した後、一番左に (x× y)%10 を挿入する
    # なお、a%b は a を b で割った余りを意味します。
    # K=0,1,...,9 について、以下の問題に答えてください。
    # 操作手順としてあり得るものは 2^{N-1} 通りありますが、このうち最終的に残る値が K となる操作手順は何通りありますか？
    # 答えは非常に大きくなる可能性があるので、998244353 で割った余りを求めてください。

    # 0 以上 9 以下の整数からなる長さ N の数列 A=(A_1,...,A_N) があり、この順に左から右に並んでいます。
    # 数列の長さが 1 になるまで、操作 F または操作 G を繰り返し行います。
    # 操作 F ：左端の 2 つの値 ( x,y とする ) を削除した後、一番左に (x+y)%10 を挿入する
    # 操作 G ：左

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[[0 for _ in range(10)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i][A[i]] = 1
    for i in range(N):
        for j in range(N-i-1):
            for k in range(10):
                dp[j][j+i+1][(k+A[j+i+1])%10] += dp[j][j+i][k]
                dp[j][j+i+1][(k*A[j+i+1])%10] += dp[j][j+i][k]
                dp[j][j+i+1][k] %= 998244353
    for i in range(10):
        print(dp[0][N-1][i]%998244353)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = pow(2, N - 1, 998244353)
        for j in range(N):
            if A[j] == i:
                ans[i] -= pow(2, N - j - 1, 998244353)
    for i in range(10):
        print(ans[i] % 998244353)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*10
    for i in range(10):
        ans[i] = pow(2, N-1, 998244353)
        for j in range(N):
            if A[j] == i:
                ans[i] -= pow(2, N-1-j, 998244353)
                break
    for i in range(10):
        print(ans[i]%998244353)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = [0]*10
    for i in range(10):
        tmp = 0
        for j in range(N):
            if i == A[j]:
                tmp += pow(2,N-j-1,mod)
        ans[i] = tmp%mod
    print(*ans,sep='

')

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    def read_int():
        return int(input())
    def read_int_n():
        return list(map(int, input().split()))
    def read_int_n2(N):
        return [int(input()) for _ in range(N)]
    def read_int_n3(N):
        return [read_int_n() for _ in range(N)]
    def debug(*x):
        print(*x, file=sys.stderr)
    import math

    MOD = 998244353
    N = read_int()
    A = read_int_n()
    ans = [0]*10
    ans[A[0]] += 1
    for i in range(1,N):
        ans2 = [0]*10
        for j in range(10):
            ans2[(j+A[i])%10] += ans[j]
            ans2[(j*A[i])%10] += ans[j]
        for j in range(10):
            ans[j] = ans2[j]%MOD
    for i in range(10):
        print(ans[i])

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 998244353

    # 0 から 9 までの個数を数える
    cnt = [0] * 10
    for a in A:
        cnt[a] += 1

    # 0 から 9 までの個数の累積和をとる
    cum = [0] * 11
    for i in range(10):
        cum[i + 1] = cum[i] + cnt[i]

    # 操作 F と操作 G の両方を試す
    for k in range(10):
        res = 1
        for i in range(10):
            # 操作 F で削除される個数
            n1 = cum[min(i + k, 10)] - cum[i]
            # 操作 G で削除される個数
            n2 = cum[min(i * k % 10 + 10, 10)] - cum[i * k % 10]
            # 両方の操作で削除される個数
            n = n1 + n2
            res = res * pow(2, n, mod) % mod
        print(res)

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 操作 F で出てくる数の出現回数を数える
    F_cnt = [0] * 10
    for i in range(N):
        F_cnt[(A[i] + A[i + 1]) % 10] += 1
    # 操作 G で出てくる数の出現回数を数える
    G_cnt = [0] * 10
    for i in range(N):
        G_cnt[(A[i] * A[i + 1]) % 10] += 1
    # 最終的に残る値が K となる操作手順は何通りあるか
    # まず、操作 F と操作 G の組み合わせを考える
    # 操作 F と操作 G は独立なので、
    # F が i 回、G が j 回（i+j=N-1）出てくる組み合わせは
    # (N-1)C(i) = (N-1)! / (i! * (N-1-i)!) 通りある
    # また、操作 F と操作 G はどちらも 2^{N-1} 通りあるので、
    # 最終的に残る値が K となる操作手順は
    # (N-1)C(i) * 2^{N-1} * 2^{N-1} = (N-1)! / (i! * (N-1-i)!) * 2^{2N-2} 通りある
    # 以上より、最終的に残る値が K となる操作手順は
    # (N-1)! / (i! * (N-1-i)!) * 2^{2N-2} * F_cnt[K] * G_cnt[K] 通りある
    # ただし、i=0 かつ j=0
