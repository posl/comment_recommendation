def main():
    x, y, d = map(int, input().split())
    d = d * math.pi / 180
    print(x * math.cos(d) - y * math.sin(d), x * math.sin(d) + y * math.cos(d))
