def divisors(n):
    d = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if i*i != n:
                d.append(n//i)
        i += 1
    d.sort()
    return d
N = int(input())
d = divisors(N)
for i in range(len(d)):
    print(d[i])
