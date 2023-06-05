def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i < k:
            continue
        else:
            ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()