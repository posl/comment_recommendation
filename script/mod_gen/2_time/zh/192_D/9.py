def func(x, m):
    d = max([int(i) for i in x])
    x = int(x)
    if x <= m:
        return 1
    else:
        return 0
x = input()
m = int(input())
print(func(x, m))
