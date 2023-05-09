def inner_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
