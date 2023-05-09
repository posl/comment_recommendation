def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        ok = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                ans += 1
                ok = False
                break
        if ok:
            break
    while True:
        ok = True
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] //= 3
                ans += 1
                ok = False
                break
        if ok:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    solve()