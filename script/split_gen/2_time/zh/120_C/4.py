def max_cube(s):
    if len(s) == 0:
        return 0
    red = s.count('0')
    blue = s.count('1')
    if red == 0 or blue == 0:
        return 0
    else:
        return min(red, blue) * 2
