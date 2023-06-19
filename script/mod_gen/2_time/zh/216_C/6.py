def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n%2 == 1:
            ans = 'A' + ans
            n -= 1
        else:
            ans = 'B' + ans
            n //= 2
    print(ans)

if __name__ == '__main__':
    main()