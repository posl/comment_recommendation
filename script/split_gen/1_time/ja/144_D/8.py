def main():
    a, b, x = map(int, input().split())
    if x <= a**2 * b / 2:
        print(math.degrees(math.atan(2 * x / (a * b**2))))
    else:
        print(math.degrees(math.atan(2 * (a**2 * b - x) / (a**3 * b))))
