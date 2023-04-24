Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    W = S.count('W')
    if R == 0 or W == 0:
        print(0)
    else:
        print(min(R, W))

=======
Suggestion 2

def main():
    N = int(input())
    c = input()
    W = 0
    R = 0
    for i in range(N):
        if c[i] == 'W':
            W += 1
        else:
            R += 1
    print(min(W, R))

=======
Suggestion 3

def main():
    N = int(input())
    c = input()
    R = c.count('R')
    W = c.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    print(min(c[:R].count('W'), c[-W:].count('R')))

main()

=======
Suggestion 4

def main():
    N = int(input())
    C = list(input())
    ans = 0
    for i in range(N):
        if C[i] == 'R':
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    print(min(S[:i].count("R") + S[i:].count("W") for i in range(N+1)))

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    W = N - R
    print(min(R, W))

=======
Suggestion 7

def solve():
    N = int(input())
    S = input()
    R = S.count("R")
    W = N - R
    ans = min(R, W)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    c = input()
    ans = c.count("R")
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    c = input()
    ans = c.count('R')
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    c = input()
    print(c.count('R'))
