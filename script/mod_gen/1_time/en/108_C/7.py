def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        n = N // K
        if N % K >= K // 2:
            print((n + 1) ** 3 + n ** 3)
        else:
            print((n + 1) ** 3 + (n - 1) ** 3)
    else:
        n = N // K
        print(n ** 3)

if __name__ == '__main__':
    main()