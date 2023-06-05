Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    S = list(S)
    S.append(' ')
    count = 0
    for i in range(N):
        if S[i] != S[i + 1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def get_input():
    n = int(input())
    s = input()
    return n, s

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(1,n):
        if s[i-1] != s[i]:
            count += 1
    print(count)

=======
Suggestion 7

def solve():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)
    return 0

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    num = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            num += 1
    print(num)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1,n):
        if s[i-1] != s[i]:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    #n = int(input())
    #s = input()
    n = 10
    s = 'aabbbbaaca'
    print(s)
    print(n)
    a = s[0]
    count = 1
    for i in range(1,n):
        if s[i] != a:
            a = s[i]
            count = count + 1
    print(count)
