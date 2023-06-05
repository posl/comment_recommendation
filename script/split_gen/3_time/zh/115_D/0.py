def f(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return f(n-1,x-1)
    else:
        return a[n-1] + 1 + f(n-1,x-2-a[n-1])
a = [1]
for i in range(50):
    a.append(3 + 2 * a[i])
n,x = map(int,input().split())
print(f(n,x))
