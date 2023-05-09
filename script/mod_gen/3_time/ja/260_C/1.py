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

if __name__ == '__main__':
    calc()