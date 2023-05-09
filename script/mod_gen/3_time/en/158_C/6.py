def tax(a, b):
    for i in range(1, 1000000):
        if (i * 0.08) // 1 == a and (i * 0.1) // 1 == b:
            return i
    return -1
a, b = map(int, input().split())
print(tax(a, b))

if __name__ == '__main__':
    tax()