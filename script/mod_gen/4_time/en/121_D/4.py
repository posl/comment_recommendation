def xor(a, b):
    if a == b:
        return a
    else:
        return xor(a, (a + b) // 2) * 2 + 1
a, b = map(int, input().split())
print(xor(a, b))

if __name__ == '__main__':
    xor()