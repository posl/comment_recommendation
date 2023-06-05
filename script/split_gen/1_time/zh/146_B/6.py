def rotate(string, n):
    if n == 0:
        return string
    if n > 0:
        n = n % 26
        for i in range(n):
            string = string[1:] + string[0]
        return string
    if n < 0:
        n = abs(n) % 26
        for i in range(n):
            string = string[-1] + string[:-1]
        return string
print(rotate('ABCXYZ', 2))
print(rotate('ABCXYZ', 0))
print(rotate('abcdefghijklmnopqrstuvwxyz', 13))
