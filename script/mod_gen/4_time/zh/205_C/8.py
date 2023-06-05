def main():
    a, b, c = map(int, input().split())
    if a == b:
        print('=')
    elif c % 2 == 1:
        if a > b:
            print('>')
        else:
            print('<')
    else:
        if abs(a) > abs(b):
            print('>')
        elif abs(a) < abs(b):
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    main()