def factorize(n):
    fct = []
    b,e = 2,0
    while b*b <= n:
        while n % b == 0:
            n = n//b
            e = e+1
        if e > 0:
            fct.append((b,e))
        b,e = b+1,0
    if n > 1:
        fct.append((n,1))
    return fct
n = int(input())
fct = factorize(n)
ans = 0
for b,e in fct:
    x = 1
    while e >= x:
        e -= x
        ans += 1
        x += 1
print(ans)

if __name__ == '__main__':
    factorize()