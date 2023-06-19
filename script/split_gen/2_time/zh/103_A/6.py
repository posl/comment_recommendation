def min_cost(a):
    a.sort()
    return a[1]-a[0]+a[2]-a[1]
a = list(map(int, input().split()))
print(min_cost(a))
