def solve():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Gx * Sy + Sx * Gy) / (Sy + Gy))
