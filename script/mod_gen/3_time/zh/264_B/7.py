def main():
    row, col = map(int, input().split())
    if row % 2 == 0:
        if col % 2 == 0:
            print('black')
        else:
            print('white')
    else:
        if col % 2 == 0:
            print('white')
        else:
            print('black')
main()
