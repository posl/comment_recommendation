def f(n):
    if n==0:
        return ''
    if n%2==0:
        return f(n//2)+'B'
    else:
        return f(n-1)+'A'
print(f(int(input())))
