def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,m = map(int, input().split())
m = m//n
for i in range(m,0,-1):
    if m%i == 0:
        print(i)
        break

if __name__ == '__main__':
    gcd()