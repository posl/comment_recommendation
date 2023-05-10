def main():
    import math
    A, B, H, M = map(int, input().split())
    a = 2 * math.pi * (H / 12 + M / 720)
    b = 2 * math.pi * (M / 60)
    c = a - b
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(c)))
