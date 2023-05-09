def main():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) * 30
    m = M * 6
    d = abs(h - m)
    if d > 180:
        d = 360 - d
    d = d / 180 * math.pi
    print(math.sqrt(A * A + B * B - 2 * A * B * math.cos(d)))

if __name__ == '__main__':
    main()