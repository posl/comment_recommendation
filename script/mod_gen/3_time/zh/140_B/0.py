def add_b(a,b):
    if len(a) != len(b):
        return None
    else:
        l = len(a)
        c = []
        for i in range(l):
            c.append(a[i]+b[i])
        return c

if __name__ == '__main__':
    add_b()