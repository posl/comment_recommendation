def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    x -= n
    y -= n
    m = 10**9 + 7
    def comb(n,r):
        if n == r or r == 0:
            return 1
        if r > n-r:
            r = n-r
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator *= (n-i)
            denominator *= (i+1)
            numerator %= m
            denominator %= m
        return (numerator*pow(denominator,m-2,m))%m
    print(comb(x+y,x))

if __name__ == '__main__':
    main()