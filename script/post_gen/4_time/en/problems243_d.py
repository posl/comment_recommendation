Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()

    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans -= 1
        elif s[i] == 'R':
            ans += 1
        elif s[i] == 'U':
            ans //= 2
    print(ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "U":
            x = x // 2
        elif s[i] == "L":
            x = x * 2 - 1
        else:
            x = x * 2 + 1
    print(x)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "L":
            x = x*2 - 1
        elif s[i] == "R":
            x = x*2 + 1
        else:
            if x % 2 == 0:
                x = (x-1)//2
            else:
                x = x//2
    print(x)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()

    ans = X
    for s in S:
        if s == 'L':
            ans = ans*2-1
        elif s == 'R':
            ans = ans*2+1
        else:
            ans = ans//2
    print(ans)

=======
Suggestion 6

def main():
    # input
    n, x = map(int, input().split())
    s = input()
    # compute
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans //= 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    # output
    print(ans)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    s = input()
    print(solve(n, x, s))

=======
Suggestion 8

def main():
    import sys
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline

    N, X = map(int, input().split())
    S = input().rstrip()

    def dfs(n, x):
        if n == 0:
            return x
        elif S[n - 1] == 'U':
            return dfs(n - 1, x)
        elif S[n - 1] == 'L':
            return dfs(n - 1, x * 2)
        else:
            return dfs(n - 1, x * 2 + 1)

    print(dfs(N, X))

=======
Suggestion 9

def find_vertex(n,x,s):
    v=[x]
    for i in range(n):
        if s[i]=='U':
            v.append(v[i]//2)
        elif s[i]=='L':
            v.append(v[i]*2)
        else:
            v.append(v[i]*2+1)
    return v[n]

n,x=map(int,input().split())
s=input()
print(find_vertex(n,x,s))

=======
Suggestion 10

def get_input():
    n,x = map(int,input().split())
    s = input()
    return n,x,s
