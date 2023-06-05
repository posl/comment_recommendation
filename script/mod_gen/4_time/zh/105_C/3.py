def baseNeg2(N):
    if N == 0:
        return '0'
    res = ''
    while N != 0:
        res = str(N % 2) + res
        N = -(N // 2)
    return res

if __name__ == '__main__':
    baseNeg2()