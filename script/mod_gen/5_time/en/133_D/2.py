def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = sum(a) - sum(a[1::2]) * 2
    for i in range(1, n):
        ans[i] = a[i - 1] * 2 - ans[i - 1]
    print(*ans)

if __name__ == '__main__':
    solve()