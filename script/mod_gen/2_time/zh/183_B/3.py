def solve():
    sx,sy,gx,gy = map(int, input().split())
    ans = sx + sy * (gx - sx) / (sy + gy)
    print(ans)

if __name__ == '__main__':
    solve()