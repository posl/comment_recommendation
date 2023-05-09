def main():
    A, B, H, M = map(int, input().split())
    theta_H = 30 * (H + M / 60)
    theta_M = 6 * M
    theta = abs(theta_H - theta_M)
    print(((A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(theta)))) ** 0.5)

if __name__ == '__main__':
    main()