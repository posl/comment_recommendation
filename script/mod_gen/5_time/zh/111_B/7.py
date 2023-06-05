def f(x):
    if x % 111 == 0:
        return x
    else:
        return f(x+1)
N = int(input())
print(f(N))
