def compare_power(A, B, C):
    if A < 0 and B < 0:
        if C % 2 == 0:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
        else:
            if A > B:
                return '<'
            elif A < B:
                return '>'
            else:
                return '='
    elif A < 0 or B < 0:
        if C % 2 == 0:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
        else:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
    else:
        if A > B:
            return '>'
        elif A < B:
            return '<'
        else:
            return '='
