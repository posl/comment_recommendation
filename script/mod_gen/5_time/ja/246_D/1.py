def f(x):
    return x**3+x**2*x+x*x*x+x**3
n=int(input())
a=0
b=0
x=0
while f(x)<n:
    x+=1
    if f(x)>=n:
        break
    else:
        pass

if __name__ == '__main__':
    f()