def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            print('ARC')
        else:
            print('ABC')
