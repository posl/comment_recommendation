Synthesizing 10/10 solutions

=======
Suggestion 1

def count(s):
    c = [0]*3
    for i in range(len(s)):
        if s[i] == 'R':
            c[0] += 1
        elif s[i] == 'G':
            c[1] += 1
        else:
            c[2] += 1
    return c[0]*c[1]*c[2]

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = j * 2 - i
            if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    r = S.count('R')
    g = S.count('G')
    b = S.count('B')
    ans = r * g * b
    for i in range(N):
        for j in range(i+1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    count += 1
    print(count)

=======
Suggestion 6

def calc(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            k = 2*j - i
            if k >= n:
                continue
            if s[i] == s[k] or s[j] == s[k]:
                continue
            cnt += 1
    return cnt

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)
solve()

=======
Suggestion 9

def countRGB(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
                    count += 1
    return count

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r*g*b
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j-i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)
