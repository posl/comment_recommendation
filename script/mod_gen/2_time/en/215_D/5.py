def main():
    #input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #gcd
    import fractions
    def gcd(*numbers):
        return fractions.gcd(*numbers)
    #solve
    def solve():
        import math
        g = gcd(*A)
        if g != 1:
            return 0
        ans = 0
        for i in range(1, M+1):
            if gcd(*A, i) == 1:
                ans += 1
        return ans
    #output
    print(solve())

if __name__ == '__main__':
    main()