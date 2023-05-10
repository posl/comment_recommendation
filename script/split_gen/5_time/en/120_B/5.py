def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
a, b, k = map(int, input().split())
c = gcd(a,b)
cnt = 0
for i in range(c,0,-1):
    if c%i==0:
        cnt += 1
    if cnt==k:
        print(i)
        break
