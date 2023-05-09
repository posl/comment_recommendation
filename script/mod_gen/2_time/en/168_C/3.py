def main():
    A, B, H, M = map(int, input().split())
    theta = (H * 60 + M) * 360 / (12 * 60) - M * 360 / 60
    theta = theta / 180 * math.pi
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)))

if __name__ == '__main__':
    main()