def max_pizza_angle(N, A):
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(i+1, N):
            angle += A[j]
            if angle > 180:
                angle = 360 - angle
            if angle > max_angle:
                max_angle = angle
    return max_angle

if __name__ == '__main__':
    max_pizza_angle()