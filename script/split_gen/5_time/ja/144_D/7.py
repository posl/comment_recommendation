def main():
    a, b, x = map(int, input().split())
    if x >= a**2 * b / 2:
        print(90 - (90 * 2 * (a**2 * b - x) / (a**3)))
    else:
        print(90 * (x * 2 / (a * b)) / (b))
