def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        ans += n // i - i + 1
    print(ans)

if __name__ == '__main__':
    main()