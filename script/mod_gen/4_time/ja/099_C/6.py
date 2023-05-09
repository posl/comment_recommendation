def main():
    n = int(input())
    ans = 0
    while n > 0:
        ans += n % 6
        n //= 6
    print(ans)

if __name__ == '__main__':
    main()