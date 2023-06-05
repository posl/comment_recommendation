def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        print(90 - 2 * x / (a * b**2) * 180 / math.pi)
    else:
        print(2 * (a**2*b - x) / (a**3) * 180 / math.pi)
