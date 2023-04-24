Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for a in range(1,1000):
            for b in range(1,1000):
                if S[i] == 4*a*b+3*a+3*b:
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
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for a in range(1, 1001):
            for b in range(1, 1001):
                if 4*a*b + 3*a + 3*b == s[i]:
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
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = (S[i] - 3) // 3
        b = (S[i] - 3) // 3
        if 4 * a * b + 3 * a + 3 * b != S[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 4) // 4
        if a < 1 or b < 1:
            continue
        if s[i] == 4 * a * b + 3 * a + 3 * b:
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        while True:
            b = 1
            while True:
                if 4*a*b + 3*a + 3*b == S[i]:
                    break
                elif 4*a*b + 3*a + 3*b > S[i]:
                    count += 1
                    break
                b += 1
            if 4*a*b + 3*a + 3*b == S[i]:
                break
            a += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        a = (s - 3) // 3
        b = (s - 3) // 4
        if a <= 0 or b <= 0:
            ans += 1
            continue
        if 4 * a * b + 3 * a + 3 * b != s:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        for a in range(1, S[i]):
            for b in range(1, S[i]):
                if 4*a*b+3*a+3*b == S[i]:
                    count += 1
                    break
            else:
                continue
            break
    print(N-count)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        while a < 1000:
            b = 1
            while b < 1000:
                if 4*a*b+3*a+3*b == S[i]:
                    break
                b += 1
            a += 1
        if a == 1000 and b == 1000:
            count += 1
    print(count)
main()
