def func(h):
    if h==1:
        return 1
    else:
        return 2*func(h//2)+1
h=int(input())
print(func(h))
