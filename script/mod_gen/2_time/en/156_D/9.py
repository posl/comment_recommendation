def getModulo(n, a, b):
    MOD = 10**9 + 7
    def powModulo(x, n):
        if n == 0: return 1
        elif n == 1: return x
        elif n % 2 == 0:
            return powModulo(x*x%MOD, n//2)
        else:
            return powModulo(x*x%MOD, n//2) * x % MOD
    def combModulo(n, r):
        if r == 0: return 1
        elif r == 1: return n
        else:
            return combModulo(n, r-1) * (n-r+1) * powModulo(r, MOD-2) % MOD
    return (powModulo(2, n) - 1 - combModulo(n, a) - combModulo(n, b)) % MOD
n, a, b = map(int, input().split())
print(getModulo(n, a, b))
