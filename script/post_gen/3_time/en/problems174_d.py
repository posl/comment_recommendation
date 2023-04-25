Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
        if i < r:
            r = i + 1
        if i < w:
            w = i + 1
    print(min(r,w))

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    w = s.count('W')
    r = s.count('R')
    if w == 0 or r == 0:
        print(0)
    else:
        ans = 0
        for i in range(w):
            if s[i] == 'R':
                ans += 1
        print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return

    if c[0] == 'R':
        r -= 1
    if c[-1] == 'W':
        w -= 1

    print(min(r, w))

=======
Suggestion 4

def main():
    N = int(input())
    C = input()
    W = [0] * N
    R = [0] * N
    for i in range(N):
        if C[i] == 'W':
            W[i] = W[i-1] + 1
            R[i] = R[i-1]
        else:
            W[i] = W[i-1]
            R[i] = R[i-1] + 1
    ans = N
    for i in range(N):
        ans = min(ans, W[i] + R[N-1] - R[i])
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    c = input()
    red = c.count("R")
    white = c.count("W")
    if red == 0 or white == 0:
        print(0)
        return
    if c[0] == "R":
        print(white)
        return
    if c[-1] == "W":
        print(red)
        return
    print(min(red, white))

=======
Suggestion 6

def solve():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        return 0
    if c[0] == 'R':
        return c[1:].count('W')
    else:
        return c.count('R')

=======
Suggestion 7

def main():
    N = int(input())
    stones = input()
    R = stones.count("R")
    W = stones.count("W")
    if R == 0 or W == 0:
        print(0)
        return
    if stones[0] == "R":
        R -= 1
    else:
        W -= 1
    if stones[-1] == "W":
        W -= 1
    else:
        R -= 1
    print(min(R, W))

=======
Suggestion 8

def solution():
    n = int(input())
    stones = input()
    red = stones.count('R')
    white = stones.count('W')
    if red == 0 or white == 0:
        print(0)
    elif red == white:
        print(red)
    else:
        print(1+abs(red-white)//2)

solution()

=======
Suggestion 9

def main():
    N = int(input())
    c = list(input())
    R_count = c.count('R')
    W_count = N - R_count
    ans = 0
    for i in range(R_count):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    count = 0
    n = int(input())
    c = input()
    for i in range(n):
        if c[i] == 'W':
            count += 1
    print(count - (count // 2))
