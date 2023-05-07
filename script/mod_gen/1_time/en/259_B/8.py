def calc(a, b, d):
    import math
    d = math.radians(d)
    return -1 * (a * math.cos(d) - b * math.sin(d)), a * math.sin(d) + b * math.cos(d)

if __name__ == '__main__':
    calc()