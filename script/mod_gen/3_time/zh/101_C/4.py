def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if (a[i] - a[i - 1]) % (k - 1) != 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()