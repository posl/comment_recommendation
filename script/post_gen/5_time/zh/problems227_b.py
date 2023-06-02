Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N = int(input())
    # S = list(map(int, input().split()))
    N = 5
    S = [666, 777, 888, 777, 666]
    error = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                error += 1
    print(error)

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(1, 1001):
            if (j * (j + 1) * 4 + 3 * (j + 1) + 3 * j) == s[i]:
                break
            elif (j * (j + 1) * 4 + 3 * (j + 1) + 3 * j) > s[i]:
                count += 1
                break
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if s[i] == 4:
            cnt += 1
            continue
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    cnt += 1
    print(n - cnt)

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        while a*a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4*a*b + 3*a + 3*b == S[i]:
                    break
            a += 1
        if a*a > S[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if s[i] % 2 == 0:
            count += 1
        else:
            if s[i] % 3 == 0:
                count += 1
            else:
                if s[i] % 5 == 0:
                    count += 1
                else:
                    pass

    print(n - count)

=======
Suggestion 6

def check(a, b, s):
    if 4 * a * b + 3 * a + 3 * b == s:
        return True
    else:
        return False

n = int(input())
s = list(map(int, input().split()))
count = 0
for i in range(n):
    for a in range(1, s[i] + 1):
        for b in range(1, s[i] + 1):
            if check(a, b, s[i]):
                count += 1
print(n - count)

=======
Suggestion 7

def getArea(a,b):
    return 4*a*b+3*a+3*b

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while 4 * a * b + 3 * a + 3 * b < S[i]:
            a += 1
            if 4 * a * b + 3 * a + 3 * b >= S[i]:
                break
            b += 1
            if 4 * a * b + 3 * a + 3 * b >= S[i]:
                break
        if 4 * a * b + 3 * a + 3 * b != S[i]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    s = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        a = 1
        b = 1
        while 4*a*b+3*a+3*b <= s[i]:
            if 4*a*b+3*a+3*b == s[i]:
                cnt += 1
            b += 1
        a += 1
    print(n-cnt)

=======
Suggestion 10

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if (S[i] % 2 == 0):
            count += 1
    print(count)
