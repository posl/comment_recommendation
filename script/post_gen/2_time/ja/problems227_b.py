Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for a in range(1,1000):
            for b in range(1,1000):
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
        a = 0
        b = 0
        for j in range(1, 1001):
            for k in range(1, j+1):
                if 4*j*k+3*j+3*k == S[i]:
                    a = j
                    b = k
        if a*b == 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 0
        b = 0
        for j in range(1,1000):
            if (S[i] - 3*j) % (4*j) == 0:
                a = j
                b = (S[i] - 3*j) // (4*j)
                break
        if 4*a*b + 3*a + 3*b != S[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 3) // 4
        if a > 0 and b > 0:
            if (4 * a * b + 3 * a + 3 * b) == s[i]:
                cnt += 1
    print(n - cnt)

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
                    break
                b += 1
            if 4*a*b + 3*a + 3*b == S[i]:
                break
            elif 4*a*b + 3*a + 3*b > S[i]:
                break
            a += 1
        if 4*a*b + 3*a + 3*b != S[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        a = 1
        while True:
            b = (S[i] - 3*a) / (3 + 4*a)
            if b == int(b) and b > 0:
                break
            a += 1
        if S[i] != 4*a*b + 3*a + 3*b:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        a = (S[i] - 3) // 4
        b = (S[i] - 3) % 4
        if a > 0 and b == 0 and S[i] == (4*a*a + 3*a + 3):
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int,input().split()))
    count = 0
    for i in range(n):
        a = (s[i]-1)//3
        b = (s[i]-a*3)//4
        if s[i] != 4*a*b+3*a+3*b:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    S = list(map(int,input().split()))
    #解答
    ans = 0
    for i in range(N):
        for a in range(1,1001):
            for b in range(1,1001):
                if S[i] == 4*a*b+3*a+3*b:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

=======
Suggestion 10

def get_area(a,b):
    return 4*a*b + 3*a + 3*b
