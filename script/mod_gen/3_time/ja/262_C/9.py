def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (n+1)
    for i in range(n):
        if i + 1 + a[i] <= n:
            cnt[i+1+a[i]] += 1
        if i + 1 - a[i] >= 1:
            ans += cnt[i+1-a[i]]
    print(ans)

if __name__ == '__main__':
    main()