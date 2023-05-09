def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,m = map(int,input().split())
a = m//n
while True:
    if m%a == 0:
        print(a)
        break
    a -= 1

if __name__ == '__main__':
    gcd()