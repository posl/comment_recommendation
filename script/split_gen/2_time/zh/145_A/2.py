def getAngle(a, b, x):
    import math
    if (x == a * a * b):
        return 0
    if (x == 0):
        return 90
    if (x == a * a * b / 2):
        return 45
    if (x < a * a * b / 2):
        return math.degrees(math.atan((2 * x) / (a * b * b)))
    if (x > a * a * b / 2):
        return math.degrees(math.atan((2 * (a * a * b - x)) / (a * a * a)))
