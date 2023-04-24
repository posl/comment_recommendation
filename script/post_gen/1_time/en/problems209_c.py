Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    C = list(map(int,input().split()))
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
            continue
        if C[i] == C[i-1]:
            ans *= C[i]-1
        else:
            ans *= C[i]
        ans %= MOD
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    dp = [0 for i in range(N)]
    dp[0] = 1
    for i in range(1, N):
        if C[i] > C[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    ans = 1
    for i in range(N):
        if C[i] > i+1:
            ans = (ans * dp[i]) % mod
        else:
            ans = 0
            break
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        ans *= C[i]-i
        ans %= MOD
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 1000000007
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= mod
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= min(i + 1, c[i])
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    C = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    MOD = 10**9 + 7
    C.sort()
    if C[0] == 1:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= MOD
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    # 配列Cの最大値を求める
    max_C = max(C)
    # Cの要素の個数を数える
    C_count = [0] * (max_C + 1)
    for c in C:
        C_count[c] += 1
    # 2つ以上ある要素の個数を数える
    C_2more = 0
    for c in C_count:
        if c >= 2:
            C_2more += 1
    # 2つ以上ある要素がある場合は0
    if C_2more >= 2:
        print(0)
        return
    # 2つ以上ある要素がない場合は、Cの要素の個数を数える
    ans = 1
    for c in C_count:
        if c >= 1:
            ans = ans * c % mod
    print(ans)
