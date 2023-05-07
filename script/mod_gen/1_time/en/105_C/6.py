def main():
    n = int(input())
    if n == 0:
        print('0')
        return
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans += '0'
            n //= -2
        else:
            ans += '1'
            n = (n - 1) // -2
    print(ans[::-1])

if __name__ == '__main__':
    main()