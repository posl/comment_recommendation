Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a>>i&1:
                cnt += 1
        ans += cnt*(N-cnt)*pow(2, i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[i] ^ A[j]
            ans %= 10**9+7
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        ans += cnt * (n - cnt) * (2 ** i)
        ans %= 10 ** 9 + 7
    print(ans)
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * pow(2, i, mod)
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for k in range(60):
        cnt = 0
        for i in range(N):
            if (A[i] >> k) & 1:
                cnt += 1
        ans += (1 << k) * cnt * (N - cnt)
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in a:
            if j >> i & 1:
                cnt += 1
        ans += cnt * (n - cnt) * 2 ** i
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = 0
    for i in range(60):
        c = 0
        for j in range(N):
            if A[j] & 1 << i:
                c += 1
        ans += c * (N - c) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        for i in range(60):
            if a >> i & 1:
                d[i] += 1
    ans = 0
    for i in range(60):
        ans += ((N - d[i]) * d[i] * pow(2, i, 10 ** 9 + 7)) % (10 ** 9 + 7)
    print(ans % (10 ** 9 + 7))

=======
Suggestion 9

def main():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    # 処理
    ans = 0
    for i in range(60):
        cnt_1 = 0
        for a in A:
            if (a >> i) & 1:
                cnt_1 += 1
        ans += (2**i)*cnt_1*(N-cnt_1)
        ans %= mod
    # 出力
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    # 2進数へ
    bin_list = []
    for a in A:
        bin_list.append(bin(a)[2:])

    # 2進数の桁数を揃える
    max_len = max([len(a) for a in bin_list])
    bin_list = [a.zfill(max_len) for a in bin_list]

    # 1の数を数える
    cnt = [0] * max_len
    for a in bin_list:
        for i, b in enumerate(a[::-1]):
            if b == "1":
                cnt[i] += 1

    # 答えを求める
    ans = 0
    for i, c in enumerate(cnt):
        ans += (2 ** i) * c * (N - c)
        ans %= MOD

    print(ans)
