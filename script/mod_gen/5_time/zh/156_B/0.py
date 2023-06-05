def convert_to_base(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result
n, k = map(int, input().split())
print(len(convert_to_base(n, k)))
