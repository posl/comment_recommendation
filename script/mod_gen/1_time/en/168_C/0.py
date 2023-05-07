def main():
    A, B, H, M = map(int, input().split())
    if H == 12:
        H = 0
    if M == 60:
        M = 0
        H += 1
        if H == 12:
            H = 0
    hour_angle = 0.5 * (H * 60 + M)
    minute_angle = 6 * M
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    angle = math.radians(angle)
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(angle)))

if __name__ == '__main__':
    main()