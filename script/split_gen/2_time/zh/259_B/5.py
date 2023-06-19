def main():
    a, b, d = map(int, input().split())
    import math
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x, y)
