def rotate180(s):
    s = s[::-1]
    s = s.replace('0', 'x')
    s = s.replace('1', 'y')
    s = s.replace('6', 'z')
    s = s.replace('8', '0')
    s = s.replace('9', '1')
    s = s.replace('x', '0')
    s = s.replace('y', '1')
    s = s.replace('z', '6')
    return s
s = input()
print(rotate180(s))
