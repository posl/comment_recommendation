def main():
    r,c = map(int, input().split())
    if r%2 != 0:
        if c%2 != 0:
            print('black')
        else:
            print('white')
    else:
        if c%2 != 0:
            print('white')
        else:
            print('black')

if __name__ == '__main__':
    main()