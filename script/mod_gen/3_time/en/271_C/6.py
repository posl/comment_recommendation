def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        if a[i] > ans + 1:
            break
        ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()