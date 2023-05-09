def main():
    R, C = map(int, input().split())
    if (R * C) % 2 == 0:
        print('white')
    else:
        print('black')
