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
b=set(a)
c=[]
for i in b:
  c.append(a.count(i))
ans=0
for i in c:
  j=1
  while i>=j:
    i-=j
    j+=1
    ans+=1
print(ans)

if __name__ == '__main__':
    prime_factorize()