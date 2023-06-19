def calc(n,a,b):
    mod = 10**9+7
    ans = pow(n,2,mod)
    ans -= comb(n,a,mod)
    ans -= comb(n,b,mod)
    ans %= mod
    return ans

if __name__ == '__main__':
    calc()