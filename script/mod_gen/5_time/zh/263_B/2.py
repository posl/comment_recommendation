def getGen(n, p):
    gen = 1
    while p != 1:
        gen += 1
        p = n[p-2]
    return gen

if __name__ == '__main__':
    getGen()