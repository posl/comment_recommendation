def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] >= x:
            if k > 0:
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()