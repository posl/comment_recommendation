def split(n):
    nstr = str(n)
    nlen = len(nstr)
    if nlen == 2:
        return [nstr[0], nstr[1]]
    elif nlen == 3:
        return [nstr[0], nstr[1:]]
    result = []
    for i in range(1, nlen):
        result.append([nstr[:i], nstr[i:]])
    return result

if __name__ == '__main__':
    split()