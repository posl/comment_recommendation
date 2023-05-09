def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        cnt = 1 / n
        tmp = i
        while tmp < k:
            tmp *= 2
            cnt /= 2
        ans += cnt
    print(ans)

if __name__ == '__main__':
    main()