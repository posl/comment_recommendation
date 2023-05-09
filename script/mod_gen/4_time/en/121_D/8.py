def xor(a, b):
    if a == b:
        return a
    if a == 0:
        return xor(b, a)
    if a == 1:
        return 1 if b == 2 else 0
    if a % 2 == 0:
        return xor(a-1, b) ^ a
    if b % 2 == 0:
        return xor(a, b-1) ^ b
    return 0
a, b = map(int, input().split())
print(xor(a, b))

if __name__ == '__main__':
    xor()