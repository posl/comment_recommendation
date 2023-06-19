Synthesizing 10/10 solutions

=======
Suggestion 1

def count(s):
    r = 0
    g = 0
    b = 0
    for i in range(len(s)):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    return r, g, b

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    #print(r,g,b)
    ans = r * g * b
    for i in range(n):
        for j in range(i+1,n):
            k = j + (j - i)
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                ans -= 1
    print(ans)

=======
Suggestion 3

def solve():
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
solve()

=======
Suggestion 4

def main():
    N = input()
    S = raw_input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        if S[i] == 'G':
            G += 1
        if S[i] == 'B':
            B += 1
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k < N and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print ans

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    R = [0] * N
    G = [0] * N
    B = [0] * N
    for i in range(N):
        if i != 0:
            R[i] = R[i-1]
            G[i] = G[i-1]
            B[i] = B[i-1]
        if S[i] == 'R':
            R[i] += 1
        elif S[i] == 'G':
            G[i] += 1
        else:
            B[i] += 1
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i] != S[j]:
                if S[i] != S[j+j-i]:
                    if S[j] != S[j+j-i]:
                        ans += 1
    print(ans)

=======
Suggestion 6

def countRGB(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(j+1,len(s)):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    if j-i != k-j:
                        count += 1
    return count

=======
Suggestion 7

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
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    return ans

=======
Suggestion 8

def solve(n, s):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans += 1
    return ans

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for d in range(1, n):
            j = i + d
            k = j + d
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

solve()
