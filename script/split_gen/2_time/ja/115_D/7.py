def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    num = 2**(n+2) - 3
    if x <= 1:
        return 0
    elif x <= num:
        return burger(n-1, x-1)
    elif x == num + 1:
        return 1 + burger(n-1, x-2)
    elif x <= num * 2 + 1:
        return 1 + burger(n-1, x-num-2)
    else:
        return 2**(n+1) - 1
n, x = map(int, input().split())
print(burger(n, x))
