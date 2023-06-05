def f(k, a, b):
    a_10 = 0
    b_10 = 0
    for i in range(len(a)):
        a_10 += int(a[i]) * pow(k, len(a) - i - 1)
    for i in range(len(b)):
        b_10 += int(b[i]) * pow(k, len(b) - i - 1)
    return a_10 * b_10
k = int(input())
a, b = input().split()
print(f(k, a, b))
