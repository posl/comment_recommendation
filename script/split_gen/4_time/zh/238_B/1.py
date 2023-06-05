def get_max_angle(N, A):
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(i + j) % N]
            if angle > 180:
                angle = 360 - angle
            if angle > max_angle:
                max_angle = angle
    return max_angle
