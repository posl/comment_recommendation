def get_min_sadness(n, a):
    min_sadness = 1000000000000000000000000
    for b in range(-100, 101):
        sadness = 0
        for i in range(n):
            sadness += abs(a[i] - (b + i + 1))
        min_sadness = min(min_sadness, sadness)
    return min_sadness
n = int(input())
a = list(map(int, input().split()))
print(get_min_sadness(n, a))
