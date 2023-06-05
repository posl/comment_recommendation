def f(k):
    if k <= 2:
        return k*10+k
    else:
        return 10*f(k-2)+2
k = int(input())
print(f(k))
