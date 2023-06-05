Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = j * 2 - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')

    ans = R * G * B
    for i in range(N):
        for j in range(i+1,N):
            k = j * 2 - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    total = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                total -= 1
    print(total)

=======
Suggestion 4

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
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 5

def solution1():
    n = int(input())
    s = input()
    r = [0 for _ in range(n)]
    g = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        if s[i] == 'R':
            r[i] += 1
        elif s[i] == 'G':
            g[i] += 1
        else:
            b[i] += 1
    for i in range(1, n):
        r[i] += r[i - 1]
        g[i] += g[i - 1]
        b[i] += b[i - 1]
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if s[i] == 'R':
                if s[j] == 'G':
                    ans += b[n - 1] - b[j]
                    if j + j - i < n and s[j + j - i] == 'B':
                        ans -= 1
                elif s[j] == 'B':
                    ans += g[n - 1] - g[j]
                    if j + j - i < n and s[j + j - i] == 'G':
                        ans -= 1
            elif s[i] == 'G':
                if s[j] == 'R':
                    ans += b[n - 1] - b[j]
                    if j + j - i < n and s[j + j - i] == 'B':
                        ans -= 1
                elif s[j] == 'B':
                    ans += r[n - 1] - r[j]
                    if j + j - i < n and s[j + j - i] == 'R':
                        ans -= 1
            else:
                if s[j] == 'R':
                    ans += g[n - 1] - g[j]
                    if j + j - i < n and s[j + j - i] == 'G':
                        ans -= 1
                elif s[j] == 'G':
                    ans += r[n - 1] - r[j]
                    if j + j - i < n and s[j + j - i] == 'R':
                        ans -= 1
    print(ans)

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
        for j in range(i + 1, n):
            k = j * 2 - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 7

def solve(n,s):
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(1,n):
            k = 2 * j - i
            if k < n and k > j:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    ans -= 1
    return ans

n = int(input())
s = input()
print(solve(n,s))

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        elif S[i] == 'G':
            G += 1
        else:
            B += 1
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            k = 2 * j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    cnt += 1
    print(R*G*B - cnt)

=======
Suggestion 9

def solve(N, S):
  r = S.count('R')
  g = S.count('G')
  b = S.count('B')
  ans = r * g * b
  for i in range(N):
    for j in range(i+1,N):
      k = 2 * j - i
      if k < N:
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
          ans -= 1
  return ans

N = int(input())
S = input()
print(solve(N, S))

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i):
            k = 2 * j - i
            if k < 0:
                continue
            if k >= n:
                continue
            if s[i] == s[j]:
                continue
            if s[j] == s[k]:
                continue
            if s[k] == s[i]:
                continue
            ans -= 1
    print(ans)
