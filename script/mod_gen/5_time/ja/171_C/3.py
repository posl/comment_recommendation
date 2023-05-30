def convert(n):
    if n <= 26:
        return chr(96 + n)
    else:
        return convert((n - 1) // 26) + convert((n - 1) % 26 + 1)
n = int(input())
print(convert(n))
