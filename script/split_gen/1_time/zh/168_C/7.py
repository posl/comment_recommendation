def clock_angle(hour, minute):
    hour_angle = (hour % 12 + minute / 60.0) * 30.0
    minute_angle = minute * 6.0
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    return angle
