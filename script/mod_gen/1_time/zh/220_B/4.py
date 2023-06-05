def f(k, a, b):
    a10 = 0
    for i in range(len(a)):
        a10 += int(a[-i-1]) * (k ** i)
    b10 = 0
    for i in range(len(b)):
        b10 += int(b[-i-1]) * (k ** i)
    return a10 * b10
k = int(input())
a, b = input().split()
print(f(k, a, b))
