def main():
    n = int(input())
    n -= 1
    ans = ""
    while n >= 0:
        ans = chr(ord('a') + n % 26) + ans
        n //= 26
        n -= 1
    print(ans)

if __name__ == '__main__':
    main()