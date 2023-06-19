def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0 for _ in range(max(a) + 1)]
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(1, max(a) + 1):
        for j in range(1, max(a) + 1):
            if i % j == 0:
                if i // j <= max(a):
                    ans += cnt[i] * cnt[j] * cnt[i // j]
    print(ans)

if __name__ == '__main__':
    main()