def f(n, m, s, c):
    if m == 0:
        return -1
    if n == 1:
        if m == 1:
            return c[0]
        else:
            return -1
    if n == 2:
        if m == 1:
            return c[0] * 10 + c[1]
        elif m == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            else:
                return c[1] * 10 + c[0]
        else:
            return -1
    if n == 3:
        if m == 1:
            return c[0] * 100 + c[1] * 10 + c[2]
        elif m == 2:
            if s[0] == 1:
                return c[0] * 100 + c[1] * 10 + c[2]
            elif s[0] == 2:
                return c[1] * 100 + c[0] * 10 + c[2]
            else:
                return c[1] * 100 + c[2] * 10 + c[0]
        elif m == 3:
            if s[0] == 1:
                if s[1] == 2:
                    return c[0] * 100 + c[1] * 10 + c[2]
                else:
                    return c[0] * 100 + c[2] * 10 + c[1]
            elif s[0] == 2:
                if s[1] == 1:
                    return c[1] * 100 + c[0] * 10 + c[2]
                else:
                    return c[2] * 100 + c[0] * 10 + c[1]
            else:
                if s[1] == 1:
                    return c[1] * 100 + c[2] * 10 + c[0]
                else:
                    return c[2] * 100 + c[1] * 10 + c[0]
        else:
            return -1

if __name__ == '__main__':
    f()