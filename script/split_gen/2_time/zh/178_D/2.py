def f(s):
    if s < 3:
        return 0
    elif s == 3:
        return 1
    elif s == 4:
        return 2
    else:
        return f(s-3) + f(s-4)
s = int(input())
print(f(s) % 1000000007)
