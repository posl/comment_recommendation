def swap(a, b):
    return b, a
a, b, c = input().split()
a, b = swap(a, b)
a, c = swap(a, c)
print(a, b, c)
