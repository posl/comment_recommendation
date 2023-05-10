def solve(A, B, H, M):
    import math
    hour_angle = 2 * math.pi * H / 12 + 2 * math.pi * M / 12 / 60
    minute_angle = 2 * math.pi * M / 60
    hour_x = A * math.cos(hour_angle)
    hour_y = A * math.sin(hour_angle)
    minute_x = B * math.cos(minute_angle)
    minute_y = B * math.sin(minute_angle)
    return math.sqrt((hour_x - minute_x) ** 2 + (hour_y - minute_y) ** 2)

if __name__ == '__main__':
    solve()