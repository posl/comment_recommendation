def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] + l
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if i < r:
            ans += a[i]
        else:
            ans += min(a[i], a[r - 1])
    print(ans)

if __name__ == '__main__':
    main()