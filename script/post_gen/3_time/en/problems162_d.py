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
            if s[i] == s[j]:
                continue
            k = 2 * j - i
            if k >= n:
                continue
            if s[k] == s[i] or s[k] == s[j]:
                continue
            ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(N):
        if S[i] == 'R':
            R[i+1] = R[i]+1
            G[i+1] = G[i]
            B[i+1] = B[i]
        elif S[i] == 'G':
            R[i+1] = R[i]
            G[i+1] = G[i]+1
            B[i+1] = B[i]
        elif S[i] == 'B':
            R[i+1] = R[i]
            G[i+1] = G[i]
            B[i+1] = B[i]+1
    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if S[i-1] != S[j-1]:
                if j + (j-i) <= N:
                    if S[j-1] != S[j+(j-i)-1] and S[i-1] != S[j+(j-i)-1]:
                        ans += 1
                if j - (j-i) >= 1:
                    if S[j-1] != S[j-(j-i)-1] and S[i-1] != S[j-(j-i)-1]:
                        ans += 1
    ans += (R[N]-R[0])*(G[N]-G[0])*(B[N]-B[0])
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
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = G = B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 7

def solve():
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
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if j-i != k-j:
                    if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] != s[j]:
                k = j + (j - i)
                if k < n and s[i] != s[k] and s[j] != s[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    R = [0]
    G = [0]
    B = [0]
    for i in range(N):
        R.append(R[i] + (S[i] == "R"))
        G.append(G[i] + (S[i] == "G"))
        B.append(B[i] + (S[i] == "B"))
    ans = R[-1] * G[-1] * B[-1]
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k < N and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)
