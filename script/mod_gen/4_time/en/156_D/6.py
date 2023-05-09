def solve(n, a, b):
    MOD = 10**9 + 7
    def comb(n, r):
        if n < r: return 0
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n
        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]
        for p in range(2, r + 1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p - 1, r, p):
                    numerator[k - offset] //= pivot
                    denominator[k] //= pivot
        result = 1
        for k in range(r):
            if numerator[k] > 1: result = result * numerator[k] % MOD
        return result
    return (pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)) % MOD

if __name__ == '__main__':
    solve()