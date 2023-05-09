def check_pattern(n, m, a, b, c, d, p):
    # check whether the two toys are the same or not
    # p is a permutation of 1,...,N
    # m is the number of strings
    # a, b, c, d are arrays of length m
    # check if the permutation is valid
    if len(p) != n:
        return False
    for i in range(n):
        if p.count(i+1) != 1:
            return False
    # check if the two toys are the same or not
    # by checking if the two toys have the same number of strings between each pair of balls
    # for each pair of balls, check if the two balls are connected by a string or not
    # if the two balls are connected by a string, check if the two balls are connected by the same string in the two toys
    for i in range(m):
        if p[a[i]-1] < p[b[i]-1]:
            if p[c[i]-1] < p[d[i]-1]:
                if p[a[i]-1] == p[c[i]-1] and p[b[i]-1] == p[d[i]-1]:
                    continue
                else:
                    return False
            elif p[c[i]-1] > p[d[i]-1]:
                if p[a[i]-1] == p[d[i]-1] and p[b[i]-1] == p[c[i]-1]:
                    continue
                else:
                    return False
            else:
                return False
        elif p[a[i]-1] > p[b[i]-1]:
            if p[c[i]-1] < p[d[i]-1]:
                if p[b[i]-1] == p[c[i]-1] and p[a[i]-1] == p[d[i]-1]:
                    continue
                else:
                    return False
            elif p[c[i]-1] > p[d[i]-1]:
                if p[b[i]-1] == p[d[i]-1] and p[a[i]-1] == p[c[i]-1]:
                    continue
                else:
                    return False
            else:
                return False
        else:
            return False
    return True
