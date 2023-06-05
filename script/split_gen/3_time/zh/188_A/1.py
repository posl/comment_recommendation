def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y > 2:
            print('No')
        else:
            print('Yes')
    else:
        if y - x > 2:
            print('No')
        else:
            print('Yes')
