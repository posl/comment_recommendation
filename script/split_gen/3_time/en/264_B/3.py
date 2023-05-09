def main():
    R, C = map(int, input().split())
    if R % 2 == 0 and C % 2 == 0:
        print('black')
    elif R % 2 == 1 and C % 2 == 1:
        print('black')
    else:
        print('white')
