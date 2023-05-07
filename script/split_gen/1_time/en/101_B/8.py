def problems101_b():
    n = int(input())
    s = sum([int(x) for x in list(str(n))])
    if n%s == 0:
        print('Yes')
    else:
        print('No')
