def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    if (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1) and (x2 - x1) * (y4 - y3) == (x4 - x3) * (y3 - y2) and (x2 - x1) * (y4 - y1) == (x4 - x1) * (y2 - y1):
        print("Yes")
    else:
        print("No")
