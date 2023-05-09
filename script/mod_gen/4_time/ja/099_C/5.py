def main():
    n = int(input())
    ans = 0
    while n > 0:
        ans += n % 9
        n //= 9
    print(ans)

if __name__ == '__main__':
    main()