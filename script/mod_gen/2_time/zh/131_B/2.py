def solve():
    n, l = map(int, input().split())
    ans = 0
    if l >= 0:
        ans = (l + n - 1) * (l + n) // 2 - l * (l - 1) // 2
    else:
        if l + n - 1 >= 0:
            ans = (l + n - 1) * (l + n) // 2
        else:
            if l + n >= 0:
                ans = (l + n) * (l + n + 1) // 2 - l * (l + 1) // 2
            else:
                ans = (l + n) * (l + n + 1) // 2 - (l + n - 1) * (l + n) // 2
    print(ans)

if __name__ == '__main__':
    solve()