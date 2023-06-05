def solve(a, b, c):
    if a < 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                return '<'
            elif abs(a) < abs(b):
                return '>'
            else:
                return '='
        else:
            if abs(a) > abs(b):
                return '>'
            elif abs(a) < abs(b):
                return '<'
            else:
                return '='
    elif a < 0 and b > 0:
        if c % 2 == 0:
            return '<'
        else:
            return '<'
    elif a > 0 and b < 0:
        if c % 2 == 0:
            return '>'
        else:
            return '<'
    elif a > 0 and b > 0:
        if a > b:
            return '>'
        elif a < b:
            return '<'
        else:
            return '='

if __name__ == '__main__':
    solve()