Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    dp = [[float('inf')] * 2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + int(S[i]))
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + int(S[i]) + 1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + (10 - int(S[i]) - 1))
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + (10 - int(S[i])))
    print(min(dp[N][0], dp[N][1] + 1))

=======
Suggestion 2

def solve():
    S = input()
    N = len(S)
    dp = [[float("inf")] * 2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = int(S[i])
        dp[i+1][0] = min(dp[i][0] + s, dp[i][1] + s + 1)
        dp[i+1][1] = min(dp[i][0] + (10 - s), dp[i][1] + (9 - s))
    print(min(dp[N][0], dp[N][1] + 1))

=======
Suggestion 3

def main():
    # input
    S = input()

    # compute
    cnt = 0
    while len(S) > 1:
        if S[-1] == '0':
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        cnt += 1

    # output
    print(cnt + int(S))

=======
Suggestion 4

def main():
    S = input()
    count = 0
    while S != "0":
        if S[-1] == "0":
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        count += 1
    print(count)

=======
Suggestion 5

def solve():
    S = input()
    ans = 0
    while len(S) > 1:
        if S[-1] == "0":
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        ans += 1
    print(ans + int(S))

=======
Suggestion 6

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '1':
            ans += 1
        else:
            break
    if ans == len(S):
        print(ans)
    else:
        print(ans+1)

=======
Suggestion 7

def main():
    #input
    S = input()
    #compute
    count = 0
    while True:
        if len(S) == 1:
            count += int(S)
            break
        else:
            if S[-1] == "0":
                S = S[:-1]
            else:
                count += 10 - int(S[-1])
                S = str(int(S) + 1)
    #output
    print(count)
    return

=======
Suggestion 8

def main():
    S = input()
    S = S[::-1]
    S = list(S)
    S = [int(i) for i in S]
    n = len(S)
    dp = [[float('inf') for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        # i桁目が0の場合
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + S[i])
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + S[i] + 1)
        # i桁目が1の場合
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + 10 - S[i])
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + 10 - S[i] - 1)
    print(dp[n][0])

=======
Suggestion 9

def solve():
    S = input()
    S = S[::-1]
    ans = 0
    mod = 10**9 + 7
    for i, s in enumerate(S):
        ans = (ans + (int(s) * pow(10, i, mod)) * (i + 1)) % mod
    print(ans)

=======
Suggestion 10

def main():
    pass
