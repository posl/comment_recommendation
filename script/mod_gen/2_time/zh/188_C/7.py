def func(n, alist):
    if n == 1:
        return [alist[0], alist[1]]
    else:
        a = func(n-1, alist[0:2**(n-1)])
        b = func(n-1, alist[2**(n-1):])
        if a[0] > b[0]:
            return [a[0], min(a[1], b[0])]
        else:
            return [b[0], min(a[0], b[1])]
n = int(input())
alist = list(map(int, input().split()))
print(func(n, alist)[1])
