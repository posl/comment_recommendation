def main():
    a,b,d = map(int, input().split())
    d = d * math.pi / 180
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))
