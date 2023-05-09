Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    dp = [[float('inf') for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = int(S[i])
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+s, dp[i][1]+s+1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+s+1, dp[i][1]+s)
    print(dp[N][0])

=======
Suggestion 2

def solve():
    s = int(input())
    count = 0
    while s > 0:
        if s % 100 == 0:
            s = s // 100
        elif s % 10 == 0:
            s = s // 10
        else:
            s -= 1
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    S = input()
    n = len(S)
    dp = [[float('inf') for i in range(2)] for j in range(n+1)]
    dp[n][0] = 0
    dp[n][1] = 1
    for i in range(n-1, -1, -1):
        s = int(S[i])
        for j in range(2):
            for k in range(10):
                if j == 1 and k == 0:
                    continue
                if dp[i][j] > dp[i+1][j] + k + (10-j)*s:
                    dp[i][j] = dp[i+1][j] + k + (10-j)*s
    print(dp[0][0])

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    S = S + "0"
    S = S + "0"
    S = S + "0"
    S = S + "0"
    S = S + "0"
    ans = 0
    for i in range(len(S)-5):
        if S[i] == "0":
            ans += 1
        elif S[i] == "1":
            ans += 2
        elif S[i] == "2":
            ans += 3
        elif S[i] == "3":
            ans += 4
        elif S[i] == "4":
            ans += 5
        elif S[i] == "5":
            ans += 6
        elif S[i] == "6":
            ans += 7
        elif S[i] == "7":
            ans += 8
        elif S[i] == "8":
            ans += 9
        elif S[i] == "9":
            ans += 10
    print(ans)

main()

=======
Suggestion 5

def main():
    S = input()
    keystrokes = 0
    for i in range(len(S)):
        if S[i] == "0":
            keystrokes += 1
        else:
            keystrokes += 2
    print(keystrokes-1)

=======
Suggestion 6

def solve():
    S = input()
    S = S[::-1]
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        elif i == 1:
            ans += int(S[i]) * 2
        else:
            ans += int(S[i]) * (10 ** (i - 1)) * (i - 1) + 10 ** (i - 1)
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    ans = 10**N
    for i in range(2**(N-1)):
        tmp = 0
        for j in range(N):
            if i & (1<<j):
                tmp += int(S[j:])
                break
            else:
                tmp += int(S[j]) * 10**(N-j-1)
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    ans = N
    for i in range(2**N):
        cnt = 0
        tmp = 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                tmp = 0
            tmp = tmp * 10 + int(S[j])
        cnt += len(str(tmp))
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def solve(s):
    #print(f"solve({s})")
    if s == 0:
        return 0
    elif s % 10 == 0:
        return 1 + solve(s // 10)
    elif s % 100 == 0:
        return 1 + solve(s // 100)
    else:
        return 1 + min(solve(s - 1), solve(s - (s % 10)))

=======
Suggestion 10

def main():
    S = input()
