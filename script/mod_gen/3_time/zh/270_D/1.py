def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        if i == 0:
            ans += a[i]
        else:
            ans += a[i] - a[i-1]
    ans += n - a[-1]
    print(ans)

if __name__ == '__main__':
    main()