def main():
    x, y = map(int, input().split())
    if x*2 <= y <= x*4:
        print('Yes')
    else:
        print('No')
