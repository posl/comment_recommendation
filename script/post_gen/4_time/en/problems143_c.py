Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(1, n):
        if s[i-1] != s[i]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()

    result = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            result += 1

    print(result)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    cnt = 1

    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1

    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    s = list(s)
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    num = int(input())
    colors = input()
    prev = colors[0]
    count = 1
    for i in range(1, num):
        if prev != colors[i]:
            count += 1
            prev = colors[i]
    print(count)
