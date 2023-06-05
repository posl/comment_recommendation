def rotate_180(S):
    S = S[::-1]
    S = S.replace('0', 'x')
    S = S.replace('1', '0')
    S = S.replace('x', '1')
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    return S
print(rotate_180('0601889'))
print(rotate_180('86910'))
print(rotate_180('01010'))
