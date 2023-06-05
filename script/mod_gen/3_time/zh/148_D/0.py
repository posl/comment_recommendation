def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    if max(a) > n:
        print(-1)
        return
    for i in range(1, n):
        if a[i] > a[i-1] + 1:
            print(-1)
            return
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            continue
        else:
            ans += a[i-1]
    print(ans)
    return

if __name__ == '__main__':
    main()