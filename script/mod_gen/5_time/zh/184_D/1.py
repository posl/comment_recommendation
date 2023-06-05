def f(a,b,c):
    if a==100 or b==100 or c==100:
        return 0
    else:
        return (a/(a+b+c))*(f(a+1,b,c)+1)+(b/(a+b+c))*(f(a,b+1,c)+1)+(c/(a+b+c))*(f(a,b,c+1)+1)
a,b,c=map(int,input().split())
print(f(a,b,c))
