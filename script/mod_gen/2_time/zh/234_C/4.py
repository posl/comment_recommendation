def convert(n):
    if n == 0:
        return '0'
    ans = ''
    while n > 0:
        ans = str(n % 2) + ans
        n = n // 2
    return ans

if __name__ == '__main__':
    convert()