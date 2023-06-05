def f(x):
    return x*x+2*x+3
t = int(input())
a = f(t)+t
b = f(a)+a
c = f(b)+b
print(c)
