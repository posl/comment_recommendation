def solve(n, a):
    min1 = a[0]
    min2 = a[1]
    if min1 > min2:
        min1, min2 = min2, min1
    for i in range(2,n):
        if a[i] < min1:
            min2 = min1
            min1 = a[i]
        elif a[i] < min2:
            min2 = a[i]
    for i in range(n):
        if a[i] == min2:
            return i + 1
