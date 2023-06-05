def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
a,b,c,d = map(int, input().split())
cd = c*d//gcd(c,d)
print(b-a+1-(b//c-(a-1)//c+b//d-(a-1)//d-b//cd+(a-1)//cd))

if __name__ == '__main__':
    gcd()