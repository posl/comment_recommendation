def main():
    a, b, h, m = map(int, input().split())
    import math
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(abs(h * 30 + m * 0.5 - m * 6) * math.pi / 180))
    print(c)
