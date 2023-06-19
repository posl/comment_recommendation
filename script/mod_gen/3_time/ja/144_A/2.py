def calc(a, b):
    if 1 <= a <= 20 and 1 <= b <= 20:
        return a * b
    else:
        return -1
a, b = map(int, input().split())
print(calc(a, b))
