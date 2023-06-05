def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    while n > k:
        cnt += 1
        n = n - k + 1
    print(cnt + 1)

if __name__ == '__main__':
    main()