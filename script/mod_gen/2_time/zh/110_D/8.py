def factorization(n):
    n_origin = n
    arr = []
    tmp = 2
    while tmp * tmp <= n_origin:
        if n % tmp == 0:
            cnt = 0
            while n % tmp == 0:
                cnt += 1
                n //= tmp
            arr.append((tmp, cnt))
        tmp += 1
    if n != 1:
        arr.append((n, 1))
    if not arr:
        arr.append((n_origin, 1))
    return arr

if __name__ == '__main__':
    factorization()