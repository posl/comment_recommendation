def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y > 2:
        print('No')
    else:
        print('Yes')
