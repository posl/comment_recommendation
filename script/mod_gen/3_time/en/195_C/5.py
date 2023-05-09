def main():
    n = int(input())
    ans = 0
    for i in range(1, len(str(n))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += len(str(n)) * (n - 10 ** (len(str(n)) - 1) + 1)
    print(ans)

if __name__ == '__main__':
    main()