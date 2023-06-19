def abs_max(x):
    x.sort()
    return x[-1]-x[0]
n = int(input())
a = list(map(int,input().split()))
print(abs_max(a))
