def get_max_angle(n, angles):
    result = 0
    for i in range(n):
        angle = angles[i]
        temp = angle
        for j in range(n):
            if j == i:
                continue
            temp += angles[j]
            temp %= 360
        if temp > result:
            result = temp
    return result
