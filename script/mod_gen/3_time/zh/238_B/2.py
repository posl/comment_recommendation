def get_max_angle(num, data):
    max_angle = 0
    for i in range(num):
        angle = 0
        for j in range(num):
            angle += data[(j+i)%num]
            if angle > 180:
                angle = 360 - angle
            if angle > max_angle:
                max_angle = angle
    return max_angle

if __name__ == '__main__':
    get_max_angle()