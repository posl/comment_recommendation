def main():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) * 30
    m = M * 6
    rad = abs(h - m) * math.pi / 180
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)))
