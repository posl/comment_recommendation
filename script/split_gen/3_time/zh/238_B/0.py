def get_max_angle(n, angles):
    angles.sort()
    angles.append(angles[0] + 360)
    max_angle = 0
    for i in range(n):
        angle = angles[i + 1] - angles[i]
        if angle > max_angle:
            max_angle = angle
    return 360 - max_angle
