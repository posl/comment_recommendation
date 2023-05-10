Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X, Y = map(int, input().split())
    if N == 1:
        print(0)
        return
    dp = [0] * (N + 1)
    dp[2] = X
    for i in range(3, N + 1):
        dp[i] = min(dp[i - 1] + X, dp[i - 2] + Y)
    print(dp[N])
    return

=======
Suggestion 2

def solve():
    N,X,Y = map(int,input().split())
    def f(n):
        if n == 1:
            return 0
        elif n == 2:
            return X
        else:
            return f(n-1) + X + Y*(n-2)
    print(f(N))

=======
Suggestion 3

def get_input
  gets.chomp.split.map(&:to_i)
end

n, x, y = get_input

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    print(n,x,y)
    if n == 1:
        print(0)
        return 0
    if x == y:
        print((n-1)*x)
        return 0
    if x < y:
        print((n-1)*x)
        return 0
    if x > y:
        print((n-1)*y)
        return 0

=======
Suggestion 5

def calc(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N-1) * min(X, Y)

=======
Suggestion 6

def calc(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return x + y
    return calc(n-1, x, y) + calc(n-2, x, y)

=======
Suggestion 7

def calc(N, X, Y):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return X + Y
    else:
        return calc(N-1, X, Y) + calc(N-2, X, Y)

N, X, Y = map(int, input().split())
print(calc(N, X, Y))

=======
Suggestion 8

def count_blue(n,x,y):
    if n == 1:
        return 1
    else:
        return count_blue(n-1,x,y) + count_red(n-1,x,y)

=======
Suggestion 9

def main():
    n,x,y = map(int,input().split())
    if x > y:
        x,y = y,x
    dp = [0]*(n+1)
    dp[2] = x
    for i in range(3,n+1):
        dp[i] = min(dp[i-1]+x,dp[i//2]+y+(i%2)*x)
    print(dp[n])

=======
Suggestion 10

def solve():
    #n, x, y = map(int, input().split())
    n, x, y = 10, 5, 5
    print(n, x, y)
