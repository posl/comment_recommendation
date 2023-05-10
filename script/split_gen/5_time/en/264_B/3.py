def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print('white')
    else:
        print('black')
