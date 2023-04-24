Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            X = (X + 1) // 2
        elif s == "L":
            X = 2 * X - 1
        else:
            X = 2 * X
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = (X - 1) // 2
        elif S[i] == 'L':
            X = X * 2 - 1
        else:
            X = X * 2
    print(X)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = (X - 1) // 2
        elif S[i] == "L":
            X = X * 2 - 1
        elif S[i] == "R":
            X = X * 2 + 1
    print(X)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == "U":
            ans = (ans - 1) // 2
        elif S[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = (ans + 1) // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2
    print(ans)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    s = input()
    for i in range(n):
        if s[i] == "U":
            x = (x-2)//2 + 1
        elif s[i] == "L":
            x = x*2 - 1
        else:
            x = x*2
    print(x)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "U":
            X = X // 2
        elif S[i] == "L":
            X = X * 2 - 1
        else:
            X = X * 2
    print(X)

=======
Suggestion 8

def get_parent(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x + 1) // 2

=======
Suggestion 9

def findParent(n):
    if n%2 == 0: return n//2
    else: return (n-1)//2

=======
Suggestion 10

def solve(N,X,S):
    #print(N,X,S)
    #print(S)
    #print(N,X,S)
    for i in range(N):
        if S[i] == 'U':
            X = X//2
        elif S[i] == 'L':
            X = X*2-1
        else:
            X = X*2
    return X
