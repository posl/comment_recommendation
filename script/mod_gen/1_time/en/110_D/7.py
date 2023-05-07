def factors(n):
    """ Returns a list of all factors of n. """
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
n, m = map(int, raw_input().split())
f = factors(m)
f = sorted(f)
f = f[::-1]
dp = [0] * (m + 1)
dp[0] = 1
for i in f:
    for j in xrange(i, m + 1):
        dp[j] += dp[j - i]
        dp[j] %= 10**9 + 7
print dp[m]

if __name__ == '__main__':
    factors()