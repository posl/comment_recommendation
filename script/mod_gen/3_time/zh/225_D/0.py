def find_set(x):
    global p
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

if __name__ == '__main__':
    find_set()