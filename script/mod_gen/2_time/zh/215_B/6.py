def get_k(n):
    k = 0
    while True:
        if 2**k <= n < 2**(k+1):
            break
        k += 1
    return k

if __name__ == '__main__':
    get_k()