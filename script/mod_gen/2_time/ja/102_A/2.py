def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
print(n*2//gcd(n,2))

if __name__ == '__main__':
    gcd()