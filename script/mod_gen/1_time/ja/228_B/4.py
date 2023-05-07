def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 0
    d = set()
    while True:
        if x in d:
            print(-1)
            return
        if x == 1:
            print(ans)
            return
        d.add(x)
        x = a[x] - 1
        ans += 1

if __name__ == '__main__':
    main()