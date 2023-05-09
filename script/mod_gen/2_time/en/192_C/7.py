def g1(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

if __name__ == '__main__':
    g1()