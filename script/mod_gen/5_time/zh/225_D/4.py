def query1(l, x, y):
    if l[x-1][0] == 0 and l[y-1][1] == 0:
        l[x-1][0], l[y-1][1] = y, x
    elif l[x-1][0] == 0 and l[y-1][1] != 0:
        l[x-1][0], l[y-1][1] = l[y-1][1], x
    elif l[x-1][0] != 0 and l[y-1][1] == 0:
        l[x-1][0], l[y-1][1] = y, l[x-1][0]
    elif l[x-1][0] != 0 and l[y-1][1] != 0:
        l[x-1][0], l[y-1][1] = l[y-1][1], l[x-1][0]
    return l

if __name__ == '__main__':
    query1()