Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if (s[i] == s[j]):
                cnt += 1

    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if s[i] % 2 == 0:
            if s[i] % 4 != 0:
                count += 1
        else:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 1:
            ans += 1
            continue
        for j in range(2, s[i]):
            if s[i] % j == 0:
                ans += 1
                break
    print(n - ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if s[i] == 1:
            count += 1
        elif s[i] == 2:
            count += 1
        elif s[i] == 3:
            count += 1
        elif s[i] == 5:
            count += 1
        elif s[i] == 6:
            count += 1
        elif s[i] == 7:
            count += 1
        elif s[i] == 10:
            count += 1
        elif s[i] == 13:
            count += 1
        elif s[i] == 14:
            count += 1
        elif s[i] == 15:
            count += 1
        elif s[i] == 17:
            count += 1
        elif s[i] == 19:
            count += 1
        elif s[i] == 21:
            count += 1
        elif s[i] == 22:
            count += 1
        elif s[i] == 23:
            count += 1
        elif s[i] == 26:
            count += 1
        elif s[i] == 29:
            count += 1
        elif s[i] == 30:
            count += 1
        elif s[i] == 31:
            count += 1
        elif s[i] == 34:
            count += 1
        elif s[i] == 37:
            count += 1
        elif s[i] == 38:
            count += 1
        elif s[i] == 39:
            count += 1
        elif s[i] == 41:
            count += 1
        elif s[i] == 43:
            count += 1
        elif s[i] == 46:
            count += 1
        elif s[i] == 47:
            count += 1
        elif s[i] == 51:
            count += 1
        elif s[i] == 53:
            count += 1
        elif s[i] == 57:
            count += 1
        elif s[i] == 58:
            count += 1
        elif s

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    c = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if (a + 3) * (b + 3) == s[i] + 3:
                    c += 1
                    break
            a += 1
    print(n - c)

=======
Suggestion 6

def check(s):
    for a in range(1, 1001):
        for b in range(1, 1001):
            if s == 4*a*b+3*a+3*b:
                return True
    return False

n = int(input())
s = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if not check(s[i]):
        cnt += 1
print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if a * b == s[i] and a != b:
                    if (a + b) % 2 == 1:
                        count += 1
            a += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = list(map(int, input().split()))
    result = 0
    for i in range(n):
        a = 1
        while True:
            b = 1
            while True:
                if (4*a*b+3*a+3*b) == s[i]:
                    result += 1
                    break
                elif (4*a*b+3*a+3*b) > s[i]:
                    break
                b += 1
            if b == 1:
                break
            a += 1
    print(n-result)

=======
Suggestion 10

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if (a + 3) * (b + 3) == s[i] + 3:
                    count += 1
                    break
            a += 1
    print(n - count)
