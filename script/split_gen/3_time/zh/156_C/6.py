def min_power(n, x):
    min_p = 10000
    for i in range(1, 101):
        p = 0
        for j in range(n):
            p += (x[j] - i) ** 2
        if p < min_p:
            min_p = p
    return min_p
n = int(input())
x = list(map(int, input().split()))
print(min_power(n, x))
