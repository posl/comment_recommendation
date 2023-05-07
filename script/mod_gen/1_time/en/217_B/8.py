def main():
    # put your code here
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            if s3 == 'AGC':
                print('AHC')
            else:
                print('AGC')
        else:
            print('ARC')
    else:
        print('ABC')

if __name__ == '__main__':
    main()