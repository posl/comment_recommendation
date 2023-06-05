def func(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + func(n-1,1 + (2**(n+1)-3)//2):
        return func(n-1,x-1)
    else:
        return 2**(n)-1 + func(n-1,x-2-(2**(n+1)-3)//2)
n,x = input().split()
n = int(n)
x = int(x)
print(func(n,x))
