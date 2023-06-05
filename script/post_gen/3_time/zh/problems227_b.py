Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] % 6 == 0:
            continue
        elif s[i] % 6 == 2:
            ans += 1
        elif s[i] % 6 == 4:
            ans += 1
        elif s[i] % 6 == 5:
            ans += 2
    print(ans)

=======
Suggestion 2

def get_area(a, b):
    return 4*a*b + 3*a + 3*b

n = int(input())
s = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            count += 1
        else:
            a = (s[i] + s[j]) / 2
            b = (s[i] - s[j]) / 2
            if a > 0 and b > 0 and int(a) == a and int(b) == b:
                count += 1
print(n - count)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        if s % 2 == 0:
            ans += 1
        elif s % 3 == 0:
            ans += 1
        elif s % 5 == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
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
        while a * a <= S[i]:
            if S[i] % a == 0:
                b = S[i] / a
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            a += 1
        if a * a > S[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in s:
        if i % 2 == 0:
            if i % 4 != 0:
                count += 1
        else:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(0,N):
        a = 1
        b = 1
        while a*b < S[i]:
            if a == b:
                b += 1
            else:
                a += 1
        if a*b != S[i]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if s[i] % 3 == 0:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if S[i] % 6 == 0:
            continue
        elif S[i] % 6 == 2:
            ans += 1
        elif S[i] % 6 == 4:
            ans += 1
        elif S[i] % 6 == 5:
            ans += 1
        else:
            continue
    print(ans)

=======
Suggestion 10

def get_input():
    n = int(input())
    s = list(map(int, input().split()))
    return n, s
