def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(1, n):
        ans += a[i // 2]
    print(ans)

if __name__ == '__main__':
    solve()