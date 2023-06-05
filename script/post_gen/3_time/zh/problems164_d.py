Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    if n < 4:
        print(0)
        return
    count = 0
    for i in range(n-3):
        for j in range(i+3, n):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    # print(S)
    count = 0
    for i in range(len(S)):
        for j in range(i + 3, len(S)):
            # print(S[i:j])
            if int(S[i:j]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 3

def get_s():
    s = input()
    return s

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N-3+1):
        for j in range(i+3,N+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    mod = 2019
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if int(s[i:j+1]) % mod == 0:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+3, n):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    s = input()
    s = s[::-1]
    n = len(s)
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    num = 0
    ten = 1
    ans = 0
    for i in range(n):
        num += int(s[i]) * ten
        num %= mod
        ten = ten * 10 % mod
        ans += cnt[num]
        cnt[num] += 1
    print(ans)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+3, n):
            if int(s[i:j+1]) % 2019 == 0:
                cnt += 1

    print(cnt)

=======
Suggestion 10

def main():
    S = input()
    lenS = len(S)
    count = 0
    for i in range(lenS):
        for j in range(i,lenS):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)
