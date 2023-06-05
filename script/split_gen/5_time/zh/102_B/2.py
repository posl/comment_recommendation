def max_difference():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    return a[n-1] - a[0]
print(max_difference())
