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
        for j in range(i+1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
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
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
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
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 4

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
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
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
            k = j + (j-i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] == S[k] or S[j] == S[k]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
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
Suggestion 8

def main():
    N = int(input())
    S = input()
    #print(N,S)
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        elif S[i] == "B":
            B += 1
    #print(R,G,B)
    ans = R * G * B
    #print(ans)
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 9

def countRGB(s, s_len):
    count_r = 0
    count_g = 0
    count_b = 0
    for i in range(s_len):
        if s[i] == "R":
            count_r += 1
        elif s[i] == "G":
            count_g += 1
        elif s[i] == "B":
            count_b += 1
    return count_r, count_g, count_b

=======
Suggestion 10

def count_r(s):
    return s.count("R")
