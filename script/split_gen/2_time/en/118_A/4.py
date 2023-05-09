def addOrSubtract(a, b):
    if b % a == 0:
        return a + b
    else:
        return b - a
a, b = map(int, input().split())
print(addOrSubtract(a, b))
