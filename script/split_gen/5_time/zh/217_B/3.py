def get_missing(s1, s2, s3):
    if s1 == 'ABC':
        if s2 == 'ARC':
            return 'AGC'
        else:
            return 'ARC'
    elif s1 == 'ARC':
        if s2 == 'ABC':
            return 'AGC'
        else:
            return 'ABC'
    else:
        if s2 == 'ABC':
            return 'ARC'
        else:
            return 'ABC'
s1 = input()
s2 = input()
s3 = input()
print(get_missing(s1, s2, s3))
