Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    mod = 2019
    count = [0] * mod
    count[0] = 1
    now = 0
    ten = 1
    for i in range(n-1, -1, -1):
        now = (now + int(s[i]) * ten) % mod
        ten = (ten * 10) % mod
        count[now] += 1
    ans = 0
    for i in range(mod):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    # print(S)
    count = 0
    for i in range(len(S)):
        for j in range(i,len(S)):
            # print(S[i:j+1])
            if int(S[i:j+1])%2019 == 0:
                count += 1
    print(count)

=======
Suggestion 3

def solve(s):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    return ans

=======
Suggestion 4

def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l-3):
        for j in range(i+3,l):
            if int(s[i:j+1])%2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 6

def mod(a, b, m):
    return (a % m)*(b % m) % m

=======
Suggestion 7

def f(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if int(s[i:j]) % 2019 == 0:
                ans += 1
    return ans

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        for j in range(i, N):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        for j in range(i+3, len(S)+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    mod = 2019
    m = [0] * mod
    m[0] = 1
    t = 0
    a = 1
    for i in range(n - 1, -1, -1):
        t = (t + int(s[i]) * a) % mod
        a = a * 10 % mod
        m[t] += 1
    ans = 0
    for i in range(mod):
        ans += m[i] * (m[i] - 1) // 2
    print(ans)
