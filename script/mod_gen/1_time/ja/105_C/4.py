def calc(n):
    if n == 0:
        return '0'
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= -2
    return ans
n = int(input())
print(calc(n))

if __name__ == '__main__':
    calc()