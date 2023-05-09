def main():
    a, b, h, m = map(int, input().split())
    hour_angle = (h * 60 + m) * 360 / (12 * 60)
    minute_angle = m * 360 / 60
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    angle = angle * math.pi / 180
    print(math.sqrt(a * a + b * b - 2 * a * b * math.cos(angle)))

if __name__ == '__main__':
    main()