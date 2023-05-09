def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(i, n - 1):
            if h[j] >= h[j + 1]:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()