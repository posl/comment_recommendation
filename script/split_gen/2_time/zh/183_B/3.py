def solve():
    sx,sy,gx,gy = map(int, input().split())
    ans = sx + sy * (gx - sx) / (sy + gy)
    print(ans)
