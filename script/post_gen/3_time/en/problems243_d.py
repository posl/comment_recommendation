Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'U':
            x = x // 2
        elif s[i] == 'L':
            x = 2 * x - 1
        else:
            x = 2 * x + 1
    print(x)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = X // 2
        elif s == 'L':
            X = X * 2 - 1
        else:
            X = X * 2 + 1
    print(X)

=======
Suggestion 3

def solve(n, x, s):
    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans = ans * 2
        elif s[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = (ans - 1) // 2
    return ans

n, x = map(int, input().split())
s = input()
print(solve(n, x, s))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x = 2*x
        elif s[i] == 'R':
            x = 2*x + 1
        else:
            x = (x+1)//2
    print(x)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'L':
            X = 2 * X
        elif S[i] == 'R':
            X = 2 * X + 1
        else:
            X = (X + 1) // 2
    print(X)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = X // 2
        elif s == 'L':
            X = X * 2 - 1
        else:
            X = X * 2 + 1
    return X

print(solve())

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    s = input()

    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans = ans * 2
        elif s[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = ans // 2 + 1
    print(ans)

=======
Suggestion 8

def sol():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'U':
            x = (x+1)//2
        elif s[i] == 'L':
            x = 2*x-1
        else:
            x = 2*x
    print(x)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    S = input()
    i = 0
    while i < N:
        if S[i] == "U":
            i += 1
        elif S[i] == "L":
            X = X * 2
            i += 1
        else:
            X = X * 2 + 2
            i += 1
    print(X)

=======
Suggestion 10

def f(x, s):
    if s == '': return x
    if s[0] == 'U': return f(x//2, s[1:])
    if s[0] == 'L': return f(x//2, s[1:]) * 2
    if s[0] == 'R': return f(x//2, s[1:]) * 2 + 1

n, x = map(int, input().split())
s = input()
print(f(x, s))
