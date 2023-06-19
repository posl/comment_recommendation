def rotate180(s):
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    return s
s = input()
print(rotate180(s))
