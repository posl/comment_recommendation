def main():
    sx, sy, gx, gy = map(int, input().split())
    if sx < gx:
        print(sx + (gx - sx) * sy / (sy + gy))
    else:
        print(sx - (sx - gx) * sy / (sy + gy))
