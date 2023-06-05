def main():
    n = int(input())
    s = ''
    while n > 0:
        tmp = n % 26
        if tmp == 0:
            tmp = 26
            n -= 26
        s = chr(tmp + 96) + s
        n //= 26
    print(s)

if __name__ == '__main__':
    main()