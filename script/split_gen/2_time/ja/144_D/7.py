def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        print(90 - math.atan(2 * (a * a * b - x) / a ** 3) * 180 / math.pi)
    else:
        print(math.atan(a * b * b / 2 / x) * 180 / math.pi)
