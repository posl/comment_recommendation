Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans //= 2
        elif S[i] == 'L':
            ans = ans * 2 - 1
        elif S[i] == 'R':
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 2

def solve():
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
Suggestion 3

def solve():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == "U":
            ans //= 2
        elif S[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

solve()

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == "U":
            ans = (ans+1)//2
        elif s[i] == "L":
            ans = ans*2-1
        else:
            ans = ans*2+1
    print(ans)

=======
Suggestion 5

def get_index(n, x, s):
    index = x
    for i in range(n):
        if s[i] == 'U':
            index = index // 2
        elif s[i] == 'L':
            index = index * 2
        else:
            index = index * 2 + 1
    return index

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    S = input()
    print(S)
    print(N, X)
    print(S)
    print(N, X)
    print(S)

=======
Suggestion 7

def solve(n, x, s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans //= 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    return ans

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def get_num(n):
    num = 1
    for i in range(n):
        num *= 2
    return num

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    s = input()
    x -= 1
    for i in range(n):
        if s[i] == 'U':
            x = x // 2
        elif s[i] == 'L':
            x = x * 2
        else:
            x = x * 2 + 1
    print(x + 1)
