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
n=int(input())
a=prime_factorize(n)
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=[]
for i in b:
    j=0
    while i**j<=n:
        j+=1
    c.append(j-1)
print(sum(c))

if __name__ == '__main__':
    prime_factorize()