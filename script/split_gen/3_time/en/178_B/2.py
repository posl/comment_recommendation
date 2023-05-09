def main():
    a, b, c, d = map(int, input().split())
    if a >= 0 or b <= 0:
        print(max(a * c, a * d, b * c, b * d))
    else:
        print(max(a * c, b * d))
