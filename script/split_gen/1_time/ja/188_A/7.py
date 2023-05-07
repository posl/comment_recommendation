def main():
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if (y - x) >= 3:
        print('Yes')
    else:
        print('No')
