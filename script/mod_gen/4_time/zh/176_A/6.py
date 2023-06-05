def problem176_a():
    n,x,t = map(int,input().split())
    return (n-1)//x*t+t
print(problem176_a())
