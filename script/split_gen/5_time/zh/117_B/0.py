def judge(n, l):
    if n <= 2:
        return False
    l.sort(reverse=True)
    max_l = l[0]
