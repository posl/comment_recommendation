def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        h = (a * a * b - x) * 2 / a / a
        print(math.degrees(math.atan2(b - h, a)))
    else:
        h = x * 2 / a / b
        print(math.degrees(math.atan2(b, a - h)))
