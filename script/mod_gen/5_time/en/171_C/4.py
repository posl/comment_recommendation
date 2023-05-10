def convert_to_base_26(n):
    if n == 0:
        return 'a'
    s = ''
    while n > 0:
        n -= 1
        s = chr(ord('a') + n % 26) + s
        n //= 26
    return s

if __name__ == '__main__':
    convert_to_base_26()