def swap(a, b):
    return b, a
a, b, c = map(int, input().split())
a, b = swap(a, b)
a, c = swap(a, c)
print(a, b, c)

if __name__ == '__main__':
    swap()