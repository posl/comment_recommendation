def swap(a, b):
    a, b = b, a
    return a, b
x, y, z = map(int, input().split())
x, y = swap(x, y)
x, z = swap(x, z)
print(x, y, z)

if __name__ == '__main__':
    swap()