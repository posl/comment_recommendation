def main():
    a,b,c = map(int,input().split())
    if a == b:
        print('=')
        return
    if c % 2 == 0:
        if abs(a) == abs(b):
            print('=')
            return
        else:
            if abs(a) > abs(b):
                print('>')
            else:
                print('<')
            return
    else:
        if a > b:
            print('>')
        else:
            print('<')
        return

if __name__ == '__main__':
    main()