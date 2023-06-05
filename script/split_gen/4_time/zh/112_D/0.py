def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
n, m = map(int, input().split())
for i in range(m//n, 0, -1):
    if m%i == 0:
        print(i)
        break
