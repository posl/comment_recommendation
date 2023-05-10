def main():
    a,b,c,d = map(int,input().split())
    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    def f(x):
        return x - x//c - x//d + x//lcm(c,d)
    print(f(b)-f(a-1))
