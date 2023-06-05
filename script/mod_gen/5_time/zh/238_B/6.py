def get_max_angle(n, angles):
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += angles[(i+j)%n]
            if angle >= 360:
                angle -= 360
            if angle > max_angle:
                max_angle = angle
    return max_angle

if __name__ == '__main__':
    get_max_angle()