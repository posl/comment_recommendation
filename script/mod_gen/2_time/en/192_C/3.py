def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

if __name__ == '__main__':
    g1()