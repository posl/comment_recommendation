def solve():
    from collections import deque
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            d = min(j - i, abs(x - i) + 1 + abs(y - j))
            ans[d - 1] += 1
    print(*ans, sep='\n')

if __name__ == '__main__':
    solve()