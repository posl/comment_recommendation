def main():
    from sys import stdin
    from collections import deque
    from math import factorial
    from functools import reduce
    MOD = 10**9 + 7
    def comb(n, r):
        if n < r:
            return 0
        return factorial(n) * pow(factorial(r), MOD-2, MOD) * pow(factorial(n-r), MOD-2, MOD) % MOD
    def solve(x, y):
        if (x+y) % 3 != 0:
            return 0
        n = (x+y) // 3
        if x < n or y < n:
            return 0
        return comb(n, x-n)
    x, y = map(int, stdin.readline().split())
    print(solve(x, y))

if __name__ == '__main__':
    main()