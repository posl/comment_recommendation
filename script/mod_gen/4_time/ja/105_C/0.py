def main():
    n = int(input())
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= -2
    if ans == '':
        ans = '0'
    print(ans)

if __name__ == '__main__':
    main()