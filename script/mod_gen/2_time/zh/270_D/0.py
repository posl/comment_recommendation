def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        if i == k - 1:
            ans += n - a[i] + 1
        else:
            ans += a[i + 1] - a[i]
    print(ans)

if __name__ == '__main__':
    main()