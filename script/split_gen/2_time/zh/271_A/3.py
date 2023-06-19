def hexa(n):
    if n < 10:
        return str(n)
    else:
        return chr(ord('A') + n - 10)
n = int(input())
a = n // 16
b = n % 16
print(hexa(a) + hexa(b))
