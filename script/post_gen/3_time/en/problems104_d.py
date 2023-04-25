Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    mod = 10**9 + 7
    a = S.count('A')
    b = S.count('B')
    c = S.count('C')
    q = S.count('?')
    ans = 0
    for i, s in enumerate(S):
        if s == 'A':
            ans += (b * pow(3, q, mod) + c * pow(3, q, mod)) * pow(3, q - i, mod)
        elif s == 'B':
            ans += (a * pow(3, q, mod) + c * pow(3, q, mod)) * pow(3, q - i, mod)
        elif s == 'C':
            ans += (a * pow(3, q, mod) + b * pow(3, q, mod)) * pow(3, q - i, mod)
        else:
            ans += (a * b * pow(3, q, mod) + a * c * pow(3, q, mod) + b * c * pow(3, q, mod)) * pow(3, q - i, mod)
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    mod = 10**9 + 7
    n = len(s)
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    q = s.count('?')
    abc = a*b*c
    ans = 0
    for i in range(n):
        if s[i] == '?':
            ans += abc*(pow(3, q-1, mod)) % mod
            ans %= mod
            q -= 1
        elif s[i] == 'A':
            ans += b*c*pow(3, q, mod) % mod
            ans %= mod
        elif s[i] == 'B':
            ans += a*c*pow(3, q, mod) % mod
            ans %= mod
        elif s[i] == 'C':
            ans += a*b*pow(3, q, mod) % mod
            ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    MOD = 10**9 + 7
    Q = S.count('?')
    dp = [[0]*3 for _ in range(Q+1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        if s == '?':
            for j in range(3):
                for k in range(3):
                    dp[i+1][j] += dp[i][k]
                    dp[i+1][j] %= MOD
        else:
            for j in range(3):
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD
            if s == 'A':
                dp[i+1][1] += dp[i][0]
                dp[i+1][1] %= MOD
            elif s == 'B':
                dp[i+1][2] += dp[i][1]
                dp[i+1][2] %= MOD
            else:
                dp[i+1][0] += dp[i][2]
                dp[i+1][0] %= MOD
    print(dp[Q][0])

=======
Suggestion 4

def main():
    S = input()
    mod = 10**9 + 7
    ABC = [0, 0, 0]
    ans = 1
    for s in S:
        if s == "?":
            ans *= 3
            ans %= mod
            ABC = [ABC[0] * 3 + ABC[1] + ABC[2], ABC[0] + ABC[1] * 3 + ABC[2], ABC[0] + ABC[1] + ABC[2] * 3]
            ABC = [a % mod for a in ABC]
        else:
            ABC = [ABC[0] + ABC[1] + ABC[2], ABC[0] + ABC[1] + ABC[2], ABC[0] + ABC[1] + ABC[2]]
            ABC[ord(s) - 65] += ans
            ABC = [a % mod for a in ABC]
    print(ABC[2])

=======
Suggestion 5

def main():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        if S[i] == "A" or S[i] == "?":
            dp[i][i][0] = 1
        if S[i] == "B" or S[i] == "?":
            dp[i][i][1] = 1
        if S[i] == "C" or S[i] == "?":
            dp[i][i][2] = 1
    for i in range(N):
        for j in range(i + 1, N):
            if S[j] == "A" or S[j] == "?":
                dp[i][j][0] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
            if S[j] == "B" or S[j] == "?":
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
            if S[j] == "C" or S[j] == "?":
                dp[i][j][2] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += dp[i][j][2]
            ans %= mod
    print(ans)

=======
Suggestion 6

def ABC(S):
    ABC = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            for k in range(j+1,len(S)):
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    ABC += 1
    return ABC

S = input()
S = S.replace('?', 'A')
ABC1 = ABC(S)
S = S.replace('A', 'B')
ABC2 = ABC(S)
S = S.replace('B', 'C')
ABC3 = ABC(S)
print((ABC1 + ABC2 + ABC3) % 1000000007)

I got 50/100 points for this code. I am getting the correct answer for the first 2 test cases but not for the 3rd one. Can someone please help me with this?

I am new to the forums and I am not sure if this is the right place to post this question. I would be grateful if someone could help me with this.

Thanks in advance.

Your code is so slow, that it's not even worth optimizing. You're getting 50/100 because your code times out on the last test case. You should try to optimize your code, or use a different approach.

=======
Suggestion 7

def main():
    s = input()
    MOD = 10 ** 9 + 7
    n = len(s)
    dp = [0] * 3
    dp[0] = 1
    for i in range(n):
        if s[i] == "A":
            dp[0] += dp[0]
        elif s[i] == "B":
            dp[1] += dp[0]
        elif s[i] == "C":
            dp[2] += dp[1]
        else:
            dp[2] += 3 * dp[2] + dp[1]
            dp[1] += 3 * dp[1] + dp[0]
            dp[0] += 3 * dp[0]
        dp[0] %= MOD
        dp[1] %= MOD
        dp[2] %= MOD
    print(dp[2])

=======
Suggestion 8

def main():
    S = input()
    mod = 10 ** 9 + 7
    Q = S.count('?')
    ans = 0
    for i in range(Q):
        ans = (ans * 3 + pow(3, Q - i - 1, mod)) % mod
    print(ans)

=======
Suggestion 9

def solve():
    s = input()
    mod = 10**9 + 7

    abc = [0, 0, 0]
    cnt = 0
    for c in s:
        if c == 'A':
            abc[0] += 1
        elif c == 'B':
            abc[1] += 1
        elif c == 'C':
            abc[2] += 1
        else:
            cnt += 1

    ans = 0
    for i in range(3**cnt):
        tmp = [0, 0, 0]
        for j in range(cnt):
            tmp[i % 3] += 1
            i //= 3
        if tmp[0] == 0 or tmp[1] == 0 or tmp[2] == 0:
            continue
        ans += abc[0] * abc[1] * abc[2]
        ans %= mod
        for j in range(3):
            abc[j] += tmp[j]
    print(ans)

=======
Suggestion 10

def abc(s):
    mod = 10**9+7
    s = s.replace('?','')
    l = len(s)
    if l < 3:
        return 0
    a = 0
    b = 0
    c = 0
    for i in range(l):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += a
        elif s[i] == 'C':
            c += b
    return c%mod

S = input()
print(abc(S))
