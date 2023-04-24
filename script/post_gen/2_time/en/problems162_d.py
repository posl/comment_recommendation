Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r*g*b
    for i in range(n):
        for j in range(i+1,n):
            k = j+j-i
            if k >= n:
                break
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1
    print(ans)
main()

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = []
    G = []
    B = []
    for i in range(N):
        if S[i] == 'R':
            R.append(i)
        elif S[i] == 'G':
            G.append(i)
        else:
            B.append(i)
    ans = len(R) * len(G) * len(B)
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
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
    ans = R*G*B
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            k = j + (j-i)
            if k >= N:
                break
            if S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[k] and S[j] != S[k]:
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
    ans = R*G*B
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]:
                continue
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R*G*B
    for i in range(N):
        for j in range(i+1,N):
            k = (j-i) + j
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R*G*B
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] == S[j]:
                continue
            if S[i] == "R":
                if S[j] == "G":
                    k = "B"
                else:
                    k = "G"
            elif S[i] == "G":
                if S[j] == "R":
                    k = "B"
                else:
                    k = "R"
            elif S[i] == "B":
                if S[j] == "R":
                    k = "G"
                else:
                    k = "R"
            if j+(j-i) < N:
                if S[j+(j-i)] == k:
                    ans -= 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    r, g, b = s.count("R"), s.count("G"), s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    ans += 1
    print(ans)

main()

I think the solution is correct but it is too slow.

I think the solution is correct but it is too slow.

You can use itertools.combinations to generate all combinations. This will make your code much simpler.

from itertools import combinations

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    r = 0
    g = 0
    b = 0
    for s in S:
        if s == 'R':
            r += 1
        elif s == 'G':
            g += 1
        elif s == 'B':
            b += 1
    ans = r*g*b
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] == S[j] or S[i] == S[k] or S[j] == S[k]:
                continue
            ans -= 1
    print(ans)
