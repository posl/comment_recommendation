Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    dp = [[float('inf') for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(2):
            if j == 0:
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 1)
            else:
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + 1)
            if j == 0:
                if s[i] == '0':
                    dp[i+1][0] = min(dp[i+1][0], dp[i][j])
                else:
                    dp[i+1][1] = min(dp[i+1][1], dp[i][j])
            else:
                if s[i] == '0':
                    dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 1)
                else:
                    dp[i+1][0] = min(dp[i+1][0], dp[i][j] + 1)
    print(min(dp[n][0], dp[n][1]))

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    dp = [[float("inf")] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + int(s[i]))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + int(s[i]) + 1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + (10 - int(s[i])))
    print(dp[n][0])

=======
Suggestion 3

def main():
    S = input()
    l = len(S)
    dp = [[float("inf")] * 2 for _ in range(l+1)]
    dp[0][0] = 0
    for i in range(l):
        for j in range(2):
            n = int(S[i])
            if j == 1:
                n += 1
            dp[i+1][0] = min(dp[i+1][0], dp[i][j] + n)
            dp[i+1][1] = min(dp[i+1][1], dp[i][j] + 10 - n)
    print(min(dp[l][0], dp[l][1]+1))

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            ans += 1
        else:
            ans += int(S[i])
            if i != len(S) - 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    S = input()
    N = len(S)
    ans = N-1
    for i in range(1, 1<<N):
        t = 0
        for j in range(N):
            if i&(1<<j):
                t = t*10+int(S[j])
        if t%3==0:
            ans = min(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    S = S[::-1]
    S = S + '000'
    S = S[::-1]
    S = int(S)
    count = 0
    while S != 0:
        if S >= 100:
            count += S // 100
            S = S % 100
        elif S >= 10:
            count += S // 10
            S = S % 10
        else:
            count += S
            S = 0
    print(count)

=======
Suggestion 7

def main():
    S = input()
    from collections import deque
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        cost, num, index = queue.popleft()
        if num > int(S):
            continue
        if num == int(S):
            print(cost)
            return
        if index < len(S):
            queue.append((cost+1, num*10 + int(S[index]), index+1))
            queue.append((cost+1, num, index+1))

=======
Suggestion 8

def main():
    s = int(input())

=======
Suggestion 9

def main():
    S = input()
    print(S.count("0") + len(S))

=======
Suggestion 10

def main():
    S = input()
    print(len(S))
