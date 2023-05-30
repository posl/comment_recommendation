def harvest_nuts(n,a):
    total_nuts = 0
    for i in range(n):
        if a[i] > 10:
            total_nuts += a[i] - 10
    return total_nuts
n = int(input())
a = list(map(int, input().split()))
print(harvest_nuts(n,a))
