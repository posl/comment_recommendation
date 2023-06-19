def judge(n, l):
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        return "是"
    else:
        return "否"

if __name__ == '__main__':
    judge()