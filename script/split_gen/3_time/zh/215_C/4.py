def permute(a, k):
    if len(a) == 1:
        return a
    else:
        ret = []
        for i in range(len(a)):
            c = a[i]
            s = a[:i] + a[i+1:]
            p = permute(s, k)
            for x in p:
                ret.append(c + x)
        return ret[k-1]
