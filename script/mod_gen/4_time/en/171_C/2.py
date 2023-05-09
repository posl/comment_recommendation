def main():
    n = int(input())
    alp = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    while n > 0:
        n -= 1
        ans = alp[n%26] + ans
        n //= 26
    print(ans)

if __name__ == '__main__':
    main()