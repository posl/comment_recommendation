def main():
    x1, y1, x2, y2 = map(int, input().split())
    print("Yes" if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (x1 - y1) ** 2 == (x2 - y2) ** 2 else "No")