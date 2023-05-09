def base_neg2(N):
    if N == 0:
        return '0'
    else:
        res = ''
        while N != 0:
            res = str(N % 2) + res
            N = -(N // 2)
        return res
