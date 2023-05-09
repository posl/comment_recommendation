def swap_char(str, a, b):
    a = a - 1
    b = b - 1
    str = list(str)
    str[a], str[b] = str[b], str[a]
    return ''.join(str)
str = input()
a, b = map(int, input().split())
print(swap_char(str, a, b))
