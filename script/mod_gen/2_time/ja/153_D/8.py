def f(h):
    if h==1:
        return 1
    return 1+2*f(h//2)
h=int(input())
print(f(h))
