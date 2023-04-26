Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    return calc(n - 1, x, y) + calc(n - 2, x, y)

=======
Suggestion 2

def calc(n, x, y, memo):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = 1 + calc(n-1, x, y, memo)
    if n % 2 == 0:
        memo[n] = min(memo[n], calc(n//2, x, y, memo) + x)
    else:
        memo[n] = min(memo[n], calc(n//2, x, y, memo) + x + y)
        memo[n] = min(memo[n], calc(n//2+1, x, y, memo) + x + y)
    return memo[n]

=======
Suggestion 3

def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return x + (n - 1) * y

=======
Suggestion 4

def solve():
    #n, x, y = map(int, input().split())
    n, x, y = 10, 5, 5
    dp = [0] * (n+1)
    dp[2] = min(x, y) + 1
    for i in range(3, n+1):
        dp[i] = min(dp[i-1] + x, dp[i-2] + y) + 1
    print(dp[n])

=======
Suggestion 5

def calc(N, X, Y):
    if N == 1:
        return 0
    if N == 2:
        return X + Y
    if N == 3:
        return X * 2 + Y
    if N == 4:
        return X * 3 + Y
    if N == 5:
        return X * 4 + Y
    if N == 6:
        return X * 5 + Y
    if N == 7:
        return X * 6 + Y
    if N == 8:
        return X * 7 + Y
    if N == 9:
        return X * 8 + Y
    if N == 10:
        return X * 9 + Y
    return 0

=======
Suggestion 6

def main():
    n,x,y = map(int,input().split())
    ans = 0
    if x > y:
        ans = x*(n-1)
    else:
        ans = x*(n-1)+y*(n-2)
    print(ans)

=======
Suggestion 7

def main():
    n, x, y = map(int, input().split())
    print(n, x, y)

=======
Suggestion 8

def getNumOfBlueStone(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return getNumOfBlueStone(n - 1, x, y) + getNumOfBlueStone(n - 2, x, y)

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    print((N-1)*X if N < 2 else (N-1) * min(X, Y) + max(0, Y - X))

=======
Suggestion 10

def get_input
  gets.chomp.split.map(&:to_i)
end
