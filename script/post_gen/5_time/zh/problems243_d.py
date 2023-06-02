Synthesizing 10/10 solutions

=======
Suggestion 1

def problems243_d():
    pass

=======
Suggestion 2

def solve():
    N, X = map(int, input().split())
    S = input()
    X -= 1
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2
        elif S[i] == 'R':
            X = X * 2 + 1
    print(X + 1)

solve()

=======
Suggestion 3

def solve(n, x, s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    return ans

n, x = map(int, input().split())
s = input()
print(solve(n, x, s))

=======
Suggestion 4

def main():
    n, x = input().split()
    n = int(n)
    x = int(x)
    s = input()
    #print(n, x, s)
    result = x
    for i in range(n):
        if s[i] == 'U':
            result = result // 2
        elif s[i] == 'L':
            result = result * 2 - 1
        elif s[i] == 'R':
            result = result * 2 + 1
    print(result)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    s = input()
    x -= 1
    for i in range(n):
        if s[i] == 'U':
            x = (x - 1) // 2
        elif s[i] == 'L':
            x = x * 2 + 1
        else:
            x = x * 2 + 2
    print(x + 1)

=======
Suggestion 6

def solve(n,x,s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans//2
        elif s[i] == 'L':
            ans = ans*2 - 1
        else:
            ans = ans*2 + 1
    return ans

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    s = input()
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
Suggestion 8

def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            pass
        elif S[i] == 'R':
            ans += 2 ** (i + 1)
        else:
            ans -= 2 ** (i + 1)
    print(ans)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans = (ans + 1) // 2
        elif S[i] == 'L':
            ans = 2 * ans - 1
        else:
            ans = 2 * ans + 1
    print(ans)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    S = input()

    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans //= 2
        elif S[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)
