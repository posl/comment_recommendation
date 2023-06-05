def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 3 == 0:
        ans = int(n / 3) * y
    elif n % 3 == 1:
        ans = int(n / 3) * y + x
    else:
        ans = int(n / 3) * y + 2 * x
    print(ans)

if __name__ == '__main__':
    main()