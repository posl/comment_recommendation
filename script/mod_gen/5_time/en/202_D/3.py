def comb(a, b):
    if b == 0:
        return 1
    if a == b:
        return 1
    if a < b:
        return 0
    return comb(a-1, b-1)*a//b

if __name__ == '__main__':
    comb()