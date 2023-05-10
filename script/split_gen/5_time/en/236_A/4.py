def swap(s, a, b):
    c = list(s)
    c[a-1], c[b-1] = c[b-1], c[a-1]
    return "".join(c)
s = input()
a, b = map(int, input().split())
print(swap(s, a, b))
