def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s=int(input())
a=[s]
for i in range(1000000):
    a.append(f(a[i]))
    if a[i] in a[:i]:
        print(i+1)
        break
