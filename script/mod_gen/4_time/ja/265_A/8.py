def solve():
    x, y, n = map(int, input().split())
    ans = 10000000000
    for i in range(100):
        for j in range(100):
            if x*i + 3*j*y == n:
                ans = min(ans, i*x+j*y)
    print(ans)

if __name__ == '__main__':
    solve()