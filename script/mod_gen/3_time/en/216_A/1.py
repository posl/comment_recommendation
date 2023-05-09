def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print('{}-'.format(x))
    elif 3 <= y <= 6:
        print('{}'.format(x))
    elif 7 <= y <= 9:
        print('{}+'.format(x))

if __name__ == '__main__':
    main()