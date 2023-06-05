def solve(n, m, sc):
    if n == 1:
        if m == 1:
            return sc[0][1]
        else:
            return -1
    elif n == 2:
        if m == 1:
            return sc[0][1] * 10 + sc[1][1]
        elif m == 2:
            if sc[0][0] == 1:
                return sc[0][1] * 10 + sc[1][1]
            else:
                return sc[1][1] * 10 + sc[0][1]
        else:
            return -1
    else:
        if m == 1:
            return sc[0][1] * 100 + sc[0][1] * 10 + sc[0][1]
        elif m == 2:
            if sc[0][0] == 1:
                return sc[0][1] * 100 + sc[1][1] * 10 + sc[1][1]
            elif sc[1][0] == 1:
                return sc[1][1] * 100 + sc[0][1] * 10 + sc[0][1]
            else:
                return -1
        elif m == 3:
            if sc[0][0] == 1:
                if sc[1][0] == 2:
                    return sc[0][1] * 100 + sc[1][1] * 10 + sc[2][1]
                else:
                    return sc[0][1] * 100 + sc[2][1] * 10 + sc[1][1]
            elif sc[1][0] == 1:
                if sc[0][0] == 2:
                    return sc[1][1] * 100 + sc[0][1] * 10 + sc[2][1]
                else:
                    return sc[1][1] * 100 + sc[2][1] * 10 + sc[0][1]
            else:
                if sc[0][0] == 2:
                    return sc[2][1] * 100 + sc[0][1] * 10 + sc[1][1]
                else:
                    return sc[2][1] * 100 + sc
