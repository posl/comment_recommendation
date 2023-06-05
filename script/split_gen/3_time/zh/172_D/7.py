def f(x):
    return sum([i for i in range(1, x + 1) if x % i == 0])
n = int(input())
print(sum([i * f(i) for i in range(1, n + 1)]))
