def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5 and (x1 - y1) * (x2 - y2) != 0:
        print("Yes")
    else:
        print("No")
