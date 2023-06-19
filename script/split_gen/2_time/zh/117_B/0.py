def judge(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return '是'
    else:
        return '否'
