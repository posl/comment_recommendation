def check_sum(a, p, q, r):
    if sum(a[0:p]) == p and sum(a[p:q]) == q and sum(a[q:r]) == r:
        return True
    else:
        return False

if __name__ == '__main__':
    check_sum()