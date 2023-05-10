def find_center_angle(angles):
    angles.sort()
    angles.append(360+angles[0])
    max_angle = 0
    for i in range(len(angles)-1):
        angle = angles[i+1] - angles[i]
        if angle > max_angle:
            max_angle = angle
    return 360 - max_angle

if __name__ == '__main__':
    find_center_angle()