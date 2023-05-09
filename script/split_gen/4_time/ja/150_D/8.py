def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(map(lambda x: x//2, a))
lcm = a[0]
for i in range(1, n):
    lcm = lcm*a[i]//gcd(lcm, a[i])
for i in range(n):
    if ((lcm//a[i])//2)%2 == 0:
        print(0)
        exit()
print(m//lcm - m//(lcm*2))
