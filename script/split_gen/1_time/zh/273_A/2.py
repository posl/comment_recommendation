def func(n):
    if n==0:
        return 1
    else:
        return n*func(n-1)
n=int(input())
print(func(n))
