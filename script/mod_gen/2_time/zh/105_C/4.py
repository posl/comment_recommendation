def get_base2(n):
    if n == 0:
        return '0'
    res = ''
    while n != 0:
        res = str(n % 2) + res
        n = -(n // 2)
    return res

if __name__ == '__main__':
    get_base2()