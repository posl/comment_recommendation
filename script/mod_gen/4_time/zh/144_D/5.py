def calcAngle(a, b, x):
    return 90 - math.degrees(math.atan(2 * x / b / a ** 2))
import math
a, b, x = map(int, input().split())

if __name__ == '__main__':
    calcAngle()