def main():
    a, b, d = map(int, input().split())
    print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
