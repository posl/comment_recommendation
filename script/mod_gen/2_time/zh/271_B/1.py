def hexa(n):
    if n == 0:
        return '00'
    elif n <= 9:
        return '0' + str(n)
    elif n <= 15:
        return '0' + chr(n + 55)
    elif n <= 255:
        return chr(n // 16 + 55) + chr(n % 16 + 55)
n = int(input())
print(hexa(n))
