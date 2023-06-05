def find_nearest_num(x, p):
    if p == []:
        return x
    else:
        p.sort()
        for i in range(len(p)):
            if x < p[i]:
                return x
            elif x == p[i]:
                return x
            else:
                if i < len(p) -1:
                    if x < (p[i] + p[i+1])/2:
                        return p[i]
                else:
                    return p[i]
