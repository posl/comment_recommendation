def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
        return
    if s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
        return
    if s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
        return
    if s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
        return
    if s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
        return
    if s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
        return
    if s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
        return
    if s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
        return
    if s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
        return
    if s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
        return
    if s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
        return
    if s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
        return
    if s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
        return
    if s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
        return
    if s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
        return
    if s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
        return
    if s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
        return
    if s2 == 'AGC' and s3 == 'ARC':
        print('ABC')
        return
    return

if __name__ == '__main__':
    main()