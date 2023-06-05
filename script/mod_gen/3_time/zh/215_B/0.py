def get_max_k(n):
    k = 0
    while 2**k <= n:
        k += 1
    return k - 1

if __name__ == '__main__':
    get_max_k()