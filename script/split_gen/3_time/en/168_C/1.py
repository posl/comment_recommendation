def main():
    A, B, H, M = map(int, input().split())
    theta_h = 2 * math.pi * (H / 12 + M / 720)
    theta_m = 2 * math.pi * (M / 60)
    theta = abs(theta_h - theta_m)
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)))
