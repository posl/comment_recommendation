def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s = int(input())
a = [s]
i = 1
while True:
    if f(a[i-1]) in a:
        print(i+1)
        break
    else:
        a.append(f(a[i-1]))
        i+=1
