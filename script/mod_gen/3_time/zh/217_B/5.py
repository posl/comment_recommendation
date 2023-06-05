def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')

if __name__ == '__main__':
    main()