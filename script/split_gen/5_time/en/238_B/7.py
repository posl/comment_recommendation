def get_max_angle(angles):
    angles.sort()
    angles.reverse()
    angles.append(angles[0] + 360)
    max_angle = 0
    for i in range(len(angles)-1):
        angle = angles[i] - angles[i+1]
        if angle > max_angle:
            max_angle = angle
    return max_angle
