def sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

if __name__ == '__main__':
    sum()