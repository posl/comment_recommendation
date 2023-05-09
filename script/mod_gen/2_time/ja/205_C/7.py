def main():
    a,b,c = map(int, input().split())
    if a == b:
        print('=')
    elif c%2 == 0:
        if abs(a) > abs(b):
            print('>')
        else:
            print('<')
    else:
        if a > b:
            print('>')
        else:
            print('<')

if __name__ == '__main__':
    main()