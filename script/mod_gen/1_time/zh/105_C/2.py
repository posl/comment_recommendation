def base2(n):
    if n == 0:
        return '0'
    else:
        s = ''
        while n != 0:
            s = str(abs(n % -2)) + s
            n = (n - (n % -2)) // -2
        return s
n = int(input())
print(base2(n))
