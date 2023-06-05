def main():
    a, b, c = map(int, input().split())
    if a == b:
        print('=')
    elif a < b:
        if c % 2 == 0:
            if abs(a) == abs(b):
                print('=')
            elif abs(a) < abs(b):
                print('<')
            else:
                print('>')
        else:
            print('<')
    else:
        if c % 2 == 0:
            if abs(a) == abs(b):
                print('=')
            elif abs(a) < abs(b):
                print('<')
            else:
                print('>')
        else:
            print('>')

if __name__ == '__main__':
    main()