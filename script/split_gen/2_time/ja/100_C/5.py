def f(n):
    result = 0
    while n % 2 == 0:
        n = n / 2
        result += 1
    return result
n = int(input())
a = list(map(int, input().split()))
print(sum([f(a[i]) for i in range(n)]))
