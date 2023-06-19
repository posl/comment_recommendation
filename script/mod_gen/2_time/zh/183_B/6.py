def solve():
    sx, sy, gx, gy = map(int, input().split())
    print(sx + (gx - sx) * sy / (sy + gy))

if __name__ == '__main__':
    solve()