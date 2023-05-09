def convert_base(num, n):
    if num == 0:
        return '0'
    s = ''
    while num > 0:
        s = str(num % n) + s
        num //= n
    return s
k = int(input())
a, b = map(str, input().split())
a = int(a, k)
b = int(b, k)
print(a * b)
