def f(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + a[n-1]:
        return f(n-1,x-1)
    elif x == 2 + a[n-1]:
        return p[n-1] + 1
    elif x <= 2 + 2 * a[n-1]:
        return p[n-1] + 1 + f(n-1,x-2-a[n-1])
    elif x == 3 + 2 * a[n-1]:
        return 2 * p[n-1] + 1
    else:
        return 2 * p[n-1] + 1 + f(n-1,x-3-2*a[n-1])
n,x = map(int,input().split())
a = [0] * 51
p = [0] * 51
a[0] = 1
p[0] = 1
for i in range(1,51):
    a[i] = 2 * a[i-1] + 3
    p[i] = 2 * p[i-1] + 1
print(f(n,x))
