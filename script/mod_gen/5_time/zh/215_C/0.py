def permutation(lst):
    if len(lst) <= 1:
        return [lst]
    r = []
    for i in range(len(lst)):
        s = lst[:i] + lst[i+1:]
        p = permutation(s)
        for x in p:
            r.append(lst[i:i+1] + x)
    return r

if __name__ == '__main__':
    permutation()