def base_minus2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 != 0:
            s += '1'
            n -= 1
        else:
            s += '0'
        n //= -2
    return s[::-1]
n = int(input())
print(base_minus2(n))

if __name__ == '__main__':
    base_minus2()