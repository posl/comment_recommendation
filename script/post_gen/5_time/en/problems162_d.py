Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            k = 2 * j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r_count = 0
    g_count = 0
    b_count = 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        elif s[i] == 'G':
            g_count += 1
        else:
            b_count += 1
    total = r_count * g_count * b_count
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] == s[j]:
                continue
            if s[i] == s[k]:
                continue
            if s[j] == s[k]:
                continue
            total -= 1
    print(total)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R*G*B
    for i in range(N-1):
        for j in range(i+1, N):
            k = 2*j-i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def solve(n, s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1
    return ans

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                ans -= 1
    print(ans)
    return

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    total = R * G * B
    for i in range(1, N):
        for j in range(N):
            k = j + i
            if k >= N:
                break
            if S[j] != S[k]:
                if S[j] != S[i + k]:
                    if S[i + k] != S[k]:
                        total -= 1
    print(total)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i] != S[j]:
                for k in range(j+1, N):
                    if S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                        count += 1
    print(count)

=======
Suggestion 8

def solve(n, s):
    ans = 0
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    for i in range(n):
        for j in range(i+1, n):
            k = 2*j-i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans += 1
    return ans - (r*g*b)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j - i
            if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    c = Counter(S)
    r = c['R']
    g = c['G']
    b = c['B']

    ans = r * g * b

    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1

    print(ans)
