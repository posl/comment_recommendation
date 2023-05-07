def main():
    a, b, x = map(int, input().split())
    if x > a * a * b / 2:
        theta = math.atan((2 * (a * a * b - x) / (a * a * a)))
    else:
        theta = math.atan((a * b * b) / (2 * x))
    print(math.degrees(theta))
