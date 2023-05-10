def main():
    a,b,c,d = map(int,input().split())
    def gcd(x,y):
        if y == 0:
            return x
        else:
            return gcd(y,x%y)
    def lcm(x,y):
        return x*y//gcd(x,y)
    def f(x):
        return x-(x//c+x//d-x//lcm(c,d))
    print(f(b)-f(a-1))

if __name__ == '__main__':
    main()