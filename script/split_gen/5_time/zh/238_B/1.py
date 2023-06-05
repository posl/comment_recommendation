def get_max_angle(n, angles):
    max_angle = 0
    for i in range(n):
        angle = angles[i]
        for j in range(n):
            if i != j:
                angle += angles[j]
        if angle > max_angle:
            max_angle = angle
    return max_angle
