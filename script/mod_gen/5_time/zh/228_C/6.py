def check(n,k,ps):
    s = sorted(ps, reverse=True)
    if s[0] <= s[k-1]:
        return False
    else:
        return True

if __name__ == '__main__':
    check()