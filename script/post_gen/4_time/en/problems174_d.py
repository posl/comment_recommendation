Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    ans = 10**9
    for i in range(n):
        if s[i] == 'R':
            r -= 1
        else:
            w -= 1
        ans = min(ans, r + w)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    if R == 0 or W == 0:
        print(0)
    else:
        print(min(R,W))

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    print(min(s[:i].count('W') + s[i:].count('R') for i in range(n)))

=======
Suggestion 4

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    print(min(c[:r].count('W'), c[-w:].count('R')))

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print(0)
        else:
            print(1)
    else:
        if S[:N//2] == S[N//2+1:]:
            print(1)
        else:
            print(2)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = n - r
    print(min(r, w))

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    W = S.count('W')
    print(min(R, W))

=======
Suggestion 8

def main():
    N = int(input())
    S = list(input())
    W = S.count('W')
    R = N - W
    print(min(W, R))

main()

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    r = S.count("R")
    w = N-r
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,w))

=======
Suggestion 10

def main():
    N = int(input())
    c = input()
    print(c.count('W') + 1 - c.count('W', 0, c.find('R') + 1))
