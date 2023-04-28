Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+4, n+1):
            if int(s[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n-3):
        for j in range(i+3,n):
            if int(s[i:j+1]) % 2019 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = 0
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    d = 1
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * d) % 2019
        d = (d * 10) % 2019
        cnt[t] += 1
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    t = [0] * n
    t[n-1] = int(s[n-1])
    for i in range(n-2, -1, -1):
        t[i] = (t[i+1] + int(s[i]) * pow(10, n-i-1, 2019)) % 2019
    t.sort()
    ans = 0
    cnt = 0
    for i in range(n):
        if t[i] == 0:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    ans += cnt * (cnt + 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i+3,N+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(0, n):
        for j in range(i, n):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    m = [0] * 2019
    m[0] = 1
    t = 0
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * pow(10, i, 2019)) % 2019
        m[t] += 1

    ans = 0
    for i in m:
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(0,n):
        for j in range(i,n):
            if int(s[i:j+1])%2019 == 0:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = 0
    mod = 2019
    mod_list = [0] * mod
    mod_list[0] = 1
    num = 0
    for i in range(n):
        num = (num + int(s[n - 1 - i]) * pow(10, i, mod)) % mod
        ans += mod_list[num]
        mod_list[num] += 1
    print(ans)

=======
Suggestion 10

def get_num(s, i, j):
    return int(s[i:j+1])
