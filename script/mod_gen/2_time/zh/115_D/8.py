def func(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + func(n-1,2**(n+1)-3):
        return func(n-1,x-1)
    elif x == 2 + func(n-1,2**(n+1)-3):
        return 1 + func(n-1,2**(n+1)-3)
    elif x <= 2 + 2*func(n-1,2**(n+1)-3):
        return 1 + func(n-1,x-2-func(n-1,2**(n+1)-3))
    elif x == 3 + 2*func(n-1,2**(n+1)-3):
        return 1 + 2*func(n-1,2**(n+1)-3)
    else:
        return 2 + func(n-1,x-3-2*func(n-1,2**(n+1)-3))
n,x = map(int,input().split())
print(func(n,x))
