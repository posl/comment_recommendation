def f(a,b,c):
    return 1 + a*f(a+1,b-1,c) + b*f(a,b+1,c-1) + c*f(a,b,c+1) - (a+b+c)
a,b,c = map(int, input().split())
print(f(a,b,c))
