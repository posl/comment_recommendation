Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'L':
            X = X * 2
        elif s == 'R':
            X = X * 2 + 1
        else:
            X = (X + 1) // 2
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans * 2
        elif S[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 3

def solve():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x = x * 2
        elif s[i] == 'R':
            x = x * 2 + 2
        else:
            x = x * 2 + 1
    print(x)

solve()

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans * 2
        elif S[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = (ans - 1) // 2
    print(ans)

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for s in S:
        if s == "L":
            ans = ans * 2 - 1
        elif s == "R":
            ans = ans * 2 + 1
        else:
            ans = ans // 2
    print(ans)

=======
Suggestion 6

def solve(n,x,s):
    for i in range(n):
        if s[i]=='U':
            x=x//2
        elif s[i]=='L':
            x=2*x-1
        else:
            x=2*x+1
    return x

n,x=map(int,input().split())
s=input()
print(solve(n,x,s))

=======
Suggestion 7

def solve(n, x, s):
    p = [0] * (n + 1)
    p[0] = x
    for i in range(n):
        if s[i] == 'U':
            p[i + 1] = p[i] // 2
        elif s[i] == 'L':
            p[i + 1] = p[i] * 2 - 1
        else:
            p[i + 1] = p[i] * 2 + 1
    return p[-1]

=======
Suggestion 8

def main():
    N,X = map(int, input().split())
    S = input()

    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans - 1
        elif S[i] == 'R':
            ans = ans + 1
        elif S[i] == 'U':
            ans = ans // 2
    print(ans)

main()

=======
Suggestion 9

def main():
    # input
    N, X = map(int, input().split())
    S = input()
    # compute
    for i in range(N):
        if S[i] == 'L':
            X = 2*X
        elif S[i] == 'R':
            X = 2*X+1
        else:
            X = (X-1)//2
    # output
    print(X)

=======
Suggestion 10

def calc_vertice(n, x, s):
    current_vertice = x
    for i in range(n):
        if s[i] == 'U':
            current_vertice = current_vertice // 2
        elif s[i] == 'L':
            current_vertice = current_vertice * 2 - 1
        elif s[i] == 'R':
            current_vertice = current_vertice * 2 + 1
    return current_vertice
