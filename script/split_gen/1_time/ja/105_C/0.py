def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ''
    while n != 0:
        if n % (-2) == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= (-2)
    print(ans)
