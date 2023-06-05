def findMaxAngle(angles):
    maxAngle = 0
    for i in range(len(angles)):
        angle = angles[i]-angles[0]
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle
        if angle > maxAngle:
            maxAngle = angle
    return maxAngle
