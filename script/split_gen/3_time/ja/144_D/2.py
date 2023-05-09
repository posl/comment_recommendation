def main():
    a, b, x = map(int, input().split())
    if x < a * a * b / 2:
        ans = math.degrees(math.atan(2 * x / (a * a * b)))
    else:
        ans = math.degrees(math.atan(a * b * b / (2 * x)))
    print(ans)
