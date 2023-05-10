def main():
    a = input()
    b = input()
    c = input()
    if a == 'ABC':
        if b == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif a == 'ARC':
        if b == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if b == 'ABC':
            print('ARC')
        else:
            print('ABC')

if __name__ == '__main__':
    main()