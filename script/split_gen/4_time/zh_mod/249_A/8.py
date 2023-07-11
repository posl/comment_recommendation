def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = 0
    aoki = 0
    while (x > 0):
        if (a > 0):
            takahashi += b
            a -= 1
        if (c > 0):
            c -= 1
        if (d > 0):
            aoki += e
            d -= 1
        if (f > 0):
            f -= 1
        x -= 1
    if (takahashi
