def f(x):
    if x==0:
        return 1
    else:
        return f(int(x/2)) + f(int(x/3))
N = int(input())
print(f(N))
