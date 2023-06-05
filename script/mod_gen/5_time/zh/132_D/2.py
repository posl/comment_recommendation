def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    #计算组合数
    def comb(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return comb(n, n - r, mod)
        return comb(n - 1, r - 1) + comb(n - 1, r)
    #计算组合数的和
    def combsum(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return (n+1)*n//2
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combsum(n, n - r, mod)
        return combsum(n - 1, r - 1) + combsum(n - 1, r)
    #计算组合数的乘积
    def combmulti(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combmulti(n, n - r, mod)
        return combmulti(n - 1, r - 1) * combmulti(n - 1, r)
    #计算组合数的除法
    def combdiv(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combdiv(n, n - r, mod)
        return combdiv(n - 1, r - 1) // combdiv

if __name__ == '__main__':
    main()