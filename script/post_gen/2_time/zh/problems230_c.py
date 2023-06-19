Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i-a==j-b) or (i-a==b-j) or (a-i==j-b) or (a-i==b-j):
                print('#', end='')
            else:
                print('.', end='')
        print('')

=======
Suggestion 2

def print_grid(n, a, b, p, q, r, s):
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i-a) == (j-b) or (i-a) == -(j-b):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if (i - a) == (j - b) or (i - a) == (b - j):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    a -= 1
    b -= 1
    p -= 1
    q -= 1
    r -= 1
    s -= 1

    ans = [['.' for _ in range(s-r+1)] for _ in range(q-p+1)]

    for i in range(max(1-a, 1-b), min(n-a, n-b)+1):
        ans[i+a-p][i+b-r] = '#'

    for i in range(max(1-a, b-n), min(n-a, b-1)+1):
        ans[i+a-p][r+b-i] = '#'

    for i in range(q-p+1):
        print(''.join(ans[i]))

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())

    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i+a-j >= 1 and i+a-j <= n) or (i+a+j >= 1 and i+a+j <= n) or (i-a+j >= 1 and i-a+j <= n) or (i-a-j >= 1 and i-a-j <= n):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 7

def printGrid(N, A, B, P, Q, R, S):
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A+i<=N and B+j<=N) or (A+i<=N and B-j>=1) or (A-i>=1 and B+j<=N) or (A-i>=1 and B-j>=1):
                print("#", end="")
            else:
                print(".", end="")
        print("")

=======
Suggestion 8

def solve():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A+i)%2 == (B+j)%2:
                print("#", end="")
            else:
                print(".", end="")
        print()

solve()

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    p,q,r,s = map(int,input().split())
    for i in range(p,q+1):
        for j in range(r,s+1):
            if (i+j)%2 == (a+b)%2:
                print("#",end="")
            else:
                print(".",end="")
        print("")
