def solve():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, int(2 * x == W and 2 * y == H))

if __name__ == '__main__':
    solve()