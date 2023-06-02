Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num_of_triple(s):
    n = len(s)
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
                    num += 1
    return num

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
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1

    print(ans)

=======
Suggestion 3

def main():
    print("hello")
    return 0

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans += 1
    print(R*G*B - ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k] and j - i != k - j:
                    count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b

    for i in range(n):
        for j in range(i+1, n):
            k = j + (j - i)
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    if j - i != k - j:
                        cnt += 1
    print(cnt)

=======
Suggestion 8

def find_next_char(s, i, c):
    for j in range(i+1, len(s)):
        if s[j] != c:
            return j
    return -1

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(i+1,n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                    ans -= 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    r, g, b = 0, 0, 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)
