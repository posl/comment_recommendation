def divisors(n):
    l = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n//i)
    return l
n = int(input())
ans = 0
for i in range(1,n+1):
    if i % 2 == 1:
        if len(divisors(i)) == 8:
            ans += 1
print(ans)
