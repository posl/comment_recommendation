def solve():
    n, x = map(int, input().split())
    x *= 100
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p
        if x < 0:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    solve()