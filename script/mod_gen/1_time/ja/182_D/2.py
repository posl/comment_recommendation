def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n):
        tmp += a[i]
        ans = max(ans, tmp)
    print(ans)
    return 0

if __name__ == '__main__':
    solve()