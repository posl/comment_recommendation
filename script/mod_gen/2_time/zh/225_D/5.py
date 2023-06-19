def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

if __name__ == '__main__':
    find_set()