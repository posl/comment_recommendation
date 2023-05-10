def main():
    # Get input here
    A, B, H, M = map(int, input().strip().split())
    # Calculate result here
    hour_angle = 0.5 * (H * 60 + M)
    minute_angle = 6 * M
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    import math
    ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle)))
    # Print result here
    print(ans)

if __name__ == '__main__':
    main()