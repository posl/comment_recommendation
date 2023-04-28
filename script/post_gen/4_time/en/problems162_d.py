Synthesizing 10/10 solutions (Duplicates hidden)

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
            k = j + (j - i)
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

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
            k = j + (j - i)
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
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
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()

    r = s.count('R')
    g = s.count('G')
    b = s.count('B')

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = j + (j - i)
            if k < n and s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                cnt += 1

    print(r * g * b - cnt)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            for k in range(j+1, N):
                if S[i] == S[k] or S[j] == S[k]:
                    continue
                if j-i != k-j:
                    count += 1
    print(count)

=======
Suggestion 9

def solve():
    N=int(input())
    S=input()
    r=S.count('R')
    g=S.count('G')
    b=S.count('B')
    ans=r*g*b
    for i in range(N):
        for j in range(i+1,N):
            k=2*j-i
            if k>=N:
                continue
            if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
                ans-=1
    print(ans)
