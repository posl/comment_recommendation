def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        ans += (N // i - i + 1)
    print(ans)

if __name__ == '__main__':
    main()