def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
a,b = map(int,input().split())
print(a*b//gcd(a,b))

if __name__ == '__main__':
    gcd()