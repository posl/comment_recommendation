def solve(n, a):
    max_angle = 0
    for i in range(n):
        total_angle = 0
        for j in range(n):
            total_angle += a[(i + j) % n]
            if total_angle > 180:
                total_angle = 360 - total_angle
            if total_angle > max_angle:
                max_angle = total_angle
    return max_angle

if __name__ == '__main__':
    solve()