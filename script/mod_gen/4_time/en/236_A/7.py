def swap(s, a, b):
    s = list(s)
    a = a - 1
    b = b - 1
    s[a], s[b] = s[b], s[a]
    return ''.join(s)
s = input()
a, b = map(int, input().split())
print(swap(s, a, b))
