def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
            return
        else:
            print(-1)
            return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
            return
        elif a[0] == 2 and a[1] == 1:
            print(1)
            return
        else:
            print(-1)
            return
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] == i + 1:
            ans += 1
        else:
            print(-1)
            return
    print(n - ans)

if __name__ == '__main__':
    main()