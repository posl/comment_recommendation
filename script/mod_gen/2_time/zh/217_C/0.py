def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC':
        if S2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif S1 == 'AGC':
        if S2 == 'ABC':
            print('ARC')
        else:
            print('ABC')
    else:
        if S2 == 'ABC':
            print('AGC')
        else:
            print('ABC')

if __name__ == '__main__':
    main()