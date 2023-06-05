def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    if s3 == 'ABC':
        if s1 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s3 == 'ARC':
        if s1 == 'AGC':
            print('ABC')
        else:
            print('AGC')
    elif s3 == 'AGC':
        if s1 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    return 0
