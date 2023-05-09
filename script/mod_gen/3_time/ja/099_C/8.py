def main():
    n = int(input())
    ans = 0
    while n > 0:
        if n % 9 == 0:
            ans += 1
            n -= 9
        else:
            ans += (n % 9)
            n -= (n % 9)
    print(ans)

if __name__ == '__main__':
    main()