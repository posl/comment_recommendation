def main():
    a, b, h, m = map(int, input().split())
    print(a**2 + b**2 - 2*a*b*(math.cos(math.pi*(h/6 - m/30))))
