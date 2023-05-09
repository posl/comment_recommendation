def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    if x == y or x == -y:
        print('Yes')
    else:
        print('No')
