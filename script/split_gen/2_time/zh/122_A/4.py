def f(a,b):
    def g(x):
        if x%4==0:
            return x
        elif x%4==1:
            return 1
        elif x%4==2:
            return x+1
        else:
            return 0
    return g(b)^g(a-1)
a,b=map(int,input().split())
print(f(a,b))
