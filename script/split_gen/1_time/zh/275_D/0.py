def f(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return f(n//2)+f(n//3)
n=int(input())
print(f(n))
