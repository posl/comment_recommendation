def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c[i] = a[i] - i - 1
    c.sort()
    ans = 0
    for i in range(n):
        if i == 0 or c[i] != c[i - 1]:
            continue
        cnt = 0
        while i < n and c[i] == c[i - 1]:
            i += 1
            cnt += 1
        ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()