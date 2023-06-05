def get_s(n):
    s = ""
    while n > 0:
        n -= 1
        s = chr(ord('a') + n % 26) + s
        n //= 26
    return s
n = int(input())
print(get_s(n))
