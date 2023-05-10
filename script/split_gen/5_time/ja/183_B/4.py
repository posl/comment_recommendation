def main():
    sx, sy, gx, gy = map(int, input().split())
    if sx > gx:
        gx, sx = sx, gx
        gy, sy = sy, gy
    print(sx + (gx - sx) * sy / (sy + gy))
