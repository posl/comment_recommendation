def solve():
    sx, sy, gx, gy = map(int, input().split())
    ans = sx + (gx - sx) * (sy / (sy + gy))
    print(ans)

if __name__ == '__main__':
    solve()