def cut_rod(p,n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if p[n] >= 0:
        return p[n]
    q = -1
    for i in range(1,n+1):
        q = max(q,cut_rod(p,n-i))
    p[n] = q
    return q

if __name__ == '__main__':
    cut_rod()