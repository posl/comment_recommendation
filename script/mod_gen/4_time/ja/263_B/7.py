def parent(n, p):
    if p[n-1] == 1:
        return 1
    else:
        return 1 + parent(p[n-1], p)

if __name__ == '__main__':
    parent()