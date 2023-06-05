def get_min_sum(n, l, r, a):
    min_sum = 0
    min_sum += a[0] * l
    for i in range(1, n):
        if a[i] < a[i-1]:
            min_sum += a[i] * l
        else:
            min_sum += a[i] * r
    return min_sum
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(get_min_sum(n, l, r, a))
