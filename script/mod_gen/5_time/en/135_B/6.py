def swap(i, j, p):
    tmp = p[i]
    p[i] = p[j]
    p[j] = tmp
    return p

if __name__ == '__main__':
    swap()