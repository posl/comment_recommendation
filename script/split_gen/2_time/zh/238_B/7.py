def max_angle(n, angle_list):
    angle_list.sort()
    max_angle = 0
    for i in range(n):
        angle = angle_list[i] - angle_list[i-1]
        if angle > max_angle:
            max_angle = angle
    return max_angle
