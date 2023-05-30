def xor(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return b ^ ((b - a) // 2) % 2
        else:
            return ((b - a) // 2) % 2
    else:
        if b % 2 == 0:
            return b ^ ((b - a + 1) // 2) % 2
        else:
            return ((b - a + 1) // 2) % 2
a, b = map(int, input().split())
print(xor(a, b))
