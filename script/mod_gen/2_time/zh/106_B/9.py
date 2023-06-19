def get_divisor(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res

if __name__ == '__main__':
    get_divisor()