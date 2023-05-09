def calc(s):
    if len(s) == 1:
        return 1
    v = s.count("v")
    w = s.count("w")
    if v == 0 or w == 0:
        return 0
    return v * w

if __name__ == '__main__':
    calc()