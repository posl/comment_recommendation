def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N=int(input())
list=prime_factorize(N)
list.sort()
count=0
tmp=0
for i in range(len(list)):
    if list[i]!=tmp:
        tmp=list[i]
        count+=1
print(count)
