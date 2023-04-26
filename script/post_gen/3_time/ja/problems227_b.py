Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for a in range(1,1001):
            for b in range(1,1001):
                if S[i] == 4*a*b + 3*a + 3*b:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 3) // 4
        if a <= 0 or b <= 0:
            continue
        if 4 * a * b + 3 * a + 3 * b == s[i]:
            continue
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if s[i] == 4 * j * k + 3 * j + 3 * k:
                    break
            else:
                continue
            break
        else:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while True:
            if 4*a*b+3*a+3*b == S[i]:
                break
            elif 4*a*b+3*a+3*b > S[i]:
                b += 1
            elif 4*a*b+3*a+3*b < S[i]:
                a += 1
        if a == b:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))

    count = 0

    for i in range(N):
        a = 1
        b = 1
        while True:
            if 4 * a * b + 3 * a + 3 * b == S[i]:
                break
            else:
                a += 1
                b = 1
                while 4 * a * b + 3 * a + 3 * b < S[i]:
                    b += 1
                    if 4 * a * b + 3 * a + 3 * b == S[i]:
                        break
            if 4 * a * b + 3 * a + 3 * b == S[i]:
                break
            if a >= 1000 and b >= 1000:
                count += 1
                break
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    a = 0
    b = 0
    count = 0
    for i in range(N):
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4*a*b + 3*a + 3*b == S[i]:
                    break
            else:
                continue
            break
        else:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while a*a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4*a*b+3*a+3*b == S[i]:
                    break
            a += 1
        if a*a > S[i]:
            count += 1
    print(count)
