def f(n):
    if n==1:
        return "A"
    elif n%2==0:
        return f(n//2)+"B"
    else:
        return f(n-1)+"A"
n=int(input())
print(f(n))
