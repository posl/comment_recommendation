def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
n,k=map(int,input().split())
print(min(n%k,k-n%k))

if __name__ == '__main__':
    gcd()