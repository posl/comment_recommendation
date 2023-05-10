def convert(x, n):
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        result = str(x % n) + result
        x //= n
    return result
X = input()
M = int(input())
d = int(max(list(X)))
