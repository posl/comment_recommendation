Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems243_d():
    pass

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    x = x - 1
    for i in range(n):
        if s[i] == 'L':
            x = x * 2
        elif s[i] == 'R':
            x = x * 2 + 2
        else:
            x = x * 2 + 1
    print(x + 1)

=======
Suggestion 3

def solve(n,x,s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    s = input()
    #print(n,x,s)
    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans -= 1
        elif s[i] == 'R':
            ans += 1
        else:
            ans = ans // 2
    print(ans)

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    S = input()
    X -= 1
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2
        else:
            X = X * 2 + 1
    print(X + 1)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'L':
            X = X * 2
        elif s == 'R':
            X = X * 2 + 1
        else:
            X = (X - 1) // 2
    print(X)

=======
Suggestion 7

def solve():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans //= 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)
