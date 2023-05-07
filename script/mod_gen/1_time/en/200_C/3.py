def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 200
    cnt[0] = 1
    for i in range(n):
        a[i] %= 200
        ans += cnt[a[i]]
        cnt[a[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()