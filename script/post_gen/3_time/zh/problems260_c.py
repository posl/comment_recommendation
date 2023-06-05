Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem260_c():
    pass

=======
Suggestion 2

def f(n,x,y):
    if n==1:
        return 0
    elif n==2:
        return x
    else:
        return f(n-1,x,y)+f(n-2,x,y)+x

n,x,y=map(int,input().split())

print(f(n,x,y))

=======
Suggestion 3

def dfs(n, x, y):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    ans = 1
    if n > 1:
        ans += dfs(n-1, x, y) + x
    if n > 2:
        for i in range(2, n):
            ans = min(ans, dfs(i, x, y) + dfs(n-i, x, y) + y)
    memo[n] = ans
    return ans

n, x, y = map(int, input().split())
memo = {}
print(dfs(n, x, y))

=======
Suggestion 4

def solve(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    if n == 4:
        return x + 2 * y
    if n == 5:
        return x + 3 * y
    if n == 6:
        return 2 * x + 4 * y
    if n == 7:
        return 2 * x + 5 * y
    if n == 8:
        return 3 * x + 6 * y
    if n == 9:
        return 3 * x + 7 * y
    if n == 10:
        return 4 * x + 8 * y

=======
Suggestion 5

def change(n,x,y):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return x+1
    if n==4:
        return x+y+1
    return change(n-1,x,y)+change(n-2,x,y)+change(n-3,x,y)+change(n-4,x,y)+x+y

=======
Suggestion 6

def main():
    n,x,y = map(int,input().split())
    ans = 0
    for i in range(1,n):
        if i <= y:
            ans += (n-i)*x
        else:
            ans += (n-i)*y
    print(ans)

=======
Suggestion 7

def main():
    n,x,y = map(int,input().split())
    print(n,x,y)

=======
Suggestion 8

def solve(n,x,y):
    if x>y:
        return 0
    else:
        return (n-1)*(y-x)
n,x,y=map(int,input().split())
print(solve(n,x,y))

=======
Suggestion 9

def main():
    pass
