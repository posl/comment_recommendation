def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'AGC':
        if s2 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    else:
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ABC')
