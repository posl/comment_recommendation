def calcSadness(a, b):
    res = 0
    for i in range(len(a)):
        res += abs(a[i] - (b + i + 1))
    return res
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = a[n // 2]
print(calcSadness(a, b))
