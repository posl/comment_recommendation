def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if n <= k:
            count += 1
            break
        else:
            n = n - k + 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()