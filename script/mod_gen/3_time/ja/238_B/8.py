def calc_max_angle(n, angles):
    angles.sort(reverse=True)
    angles.append(360 + angles[0])
    max_angle = 0
    for i in range(n):
        max_angle = max(max_angle, angles[i] - angles[i+1])
    return max_angle

if __name__ == '__main__':
    calc_max_angle()