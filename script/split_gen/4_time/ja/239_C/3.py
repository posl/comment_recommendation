def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 5:
        print('Yes')
        return
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 50:
        print('Yes')
        return
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 25:
        print('Yes')
        return
    print('No')
