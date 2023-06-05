def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s=int(input())
a=[s]
m=1
while True:
    m+=1
    a.append(f(a[m-2]))
    if a[m-1] in a[0:m-1]:
        break
print(m)
