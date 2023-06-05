def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(n):
        print(ans - cnt[a[i]] + 1)

if __name__ == '__main__':
    main()