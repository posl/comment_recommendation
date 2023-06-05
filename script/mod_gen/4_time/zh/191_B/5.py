def removeX(l, x):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        if l[0] == x:
            return []
        else:
            return l
    else:
        if l[0] == x:
            return removeX(l[1:], x)
        else:
            return [l[0]] + removeX(l[1:], x)

if __name__ == '__main__':
    removeX()