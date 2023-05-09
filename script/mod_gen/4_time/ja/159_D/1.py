def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1
    ans = 0
    for i in range(n):
        ans += (cnt[a[i]] - 1)
    for i in range(n):
        print(ans - (cnt[a[i]] - 1))

if __name__ == '__main__':
    main()