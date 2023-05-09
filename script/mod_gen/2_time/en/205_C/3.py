def main():
    a, b, c = map(int, input().split())
    if a < 0 and b > 0 and c % 2 == 1:
        print('>')
    elif a < 0 and b > 0 and c % 2 == 0:
        if abs(a) > b:
            print('>')
        elif abs(a) < b:
            print('<')
        else:
            print('=')
    elif a < 0 and b < 0:
        if abs(a) > abs(b):
            print('>')
        elif abs(a) < abs(b):
            print('<')
        else:
            print('=')
    else:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    main()