def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        elif s2 == 'AGC':
            print('ARC')
        elif s2 == 'AHC':
            print('AHC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            print('AGC')
        elif s2 == 'AGC':
            print('ABC')
        elif s2 == 'AHC':
            print('AHC')
    elif s1 == 'AGC':
        if s2 == 'ABC':
            print('ARC')
        elif s2 == 'ARC':
            print('ABC')
        elif s2 == 'AHC':
            print('AHC')
    elif s1 == 'AHC':
        if s2 == 'ABC':
            print('ARC')
        elif s2 == 'ARC':
            print('AGC')
        elif s2 == 'AGC':
            print('ABC')
