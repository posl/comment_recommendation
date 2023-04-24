Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    print(w)

=======
Suggestion 2

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        x = c.index('W')
        print(x)
    else:
        x = c.rindex('R')
        print(x)
    return

=======
Suggestion 3

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        r -= 1
    else:
        w -= 1
    if c[-1] == 'W':
        w -= 1
    else:
        r -= 1
    print(min(r, w))

=======
Suggestion 4

def main():
    n = int(input())
    c = input()
    r = c.count("R")
    w = c.count("W")
    if r == 0 or w == 0:
        print(0)
        return
    r = c[:r].count("W")
    print(r)

=======
Suggestion 5

def main():
    n = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        print(0)
    elif w == 1 or r == 1:
        print(1)
    else:
        w1 = c[:w].count('W')
        r1 = c[w:].count('R')
        print(min(w1, r1))

=======
Suggestion 6

def main():
    N = int(input())
    c = input()
    r = c.count("R")
    w = c.count("W")
    ans = min(r, w)
    for i in range(r):
        if c[i] == "W":
            ans -= 1
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    C = input()
    W = C.count('W')
    R = C.count('R')
    ans = min(W, R)
    w = 0
    r = 0
    for c in C:
        if c == 'W':
            w += 1
        else:
            r += 1
        ans = min(ans, max(w, r))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = min(r, w)

    for i in range(r):
        if c[i] == 'R':
            ans -= 1

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    c = input()
    #print(c)
    #print(c.count('W'))
    #print(c.count('R'))
    #print(c.count('RW'))
    #print(c.count('WR'))
    #print(c.count('RR'))
    #print(c.count('WW'))
    #print(c.count('WRR'))
    #print(c.count('RRW'))
    #print(c.count('RWR'))
    #print(c.count('RWW'))
    #print(c.count('WRW'))
    #print(c.count('WWR'))
    #print(c.count('WWW'))
    #print(c.count('WRRW'))
    #print(c.count('RRWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c.count('RRRR'))
    #print(c.count('WWWW'))
    #print(c.count('WWRW'))
    #print(c.count('WRRR'))
    #print(c.count('RWWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c.count('RRRR'))
    #print(c.count('WWWW'))
    #print(c.count('WWRW'))
    #print(c.count('WRRR'))
    #print(c.count('RWWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c.count('RRRR'))
    #print(c.count('WWWW'))
    #print(c.count('WWRW'))
    #print(c.count('WRRR'))
    #print(c.count('RWWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c.count('RRRR'))
    #print(c.count('WWWW'))
    #print(c.count('WWRW'))
    #print(c.count('WRRR'))
    #print(c.count('RWWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c.count('RRRR'))
    #print(c.count('WWWW'))
    #print(c.count('WWRW'))
    #print(c.count('WRRR'))
    #print(c.count('RWWW'))
    #print(c.count('RWRW'))
    #print(c.count('RRRW'))
    #print(c

=======
Suggestion 10

def main():
    N = int(input())
    c = input()

    # 0: W, 1: R
    dp = [[0 for i in range(2)] for j in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    for i in range(N):
        if c[i] == 'W':
            dp[i+1][0] = dp[i][0] + 1
            dp[i+1][1] = min(dp[i][0], dp[i][1])
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = min(dp[i][0], dp[i][1]) + 1

    print(dp[N][1])
