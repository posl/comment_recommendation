def generation(n, p):
    if n == 1:
        return 0
    else:
        return generation(p[n-2], p) + 1

if __name__ == '__main__':
    generation()