def main():
    a, b, d = map(int, input().split())
    d = d / 180 * math.pi
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))
