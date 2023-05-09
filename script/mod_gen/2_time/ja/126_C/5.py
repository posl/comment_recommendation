def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        x = i
        while x < k:
            x *= 2
            cnt += 1
        ans += 1 / n * (1/2) ** cnt
    print(ans)

if __name__ == '__main__':
    main()