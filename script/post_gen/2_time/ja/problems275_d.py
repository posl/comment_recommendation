Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)

N = int(input())
print(f(N))

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    return f(x//2) + f(x//3)

N = int(input())
print(f(N))

=======
Suggestion 3

def main():
    N = int(input())
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    for i in range(1,N+1):
        dp[i] = dp[i//2] + dp[i//3]
    print(dp[N])
