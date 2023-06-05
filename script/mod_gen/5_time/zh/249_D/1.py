def get_divisor(n):
    i = 1
    res = []
    while i*i <= n:
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
        i += 1
    res.sort()
    return res

if __name__ == '__main__':
    get_divisor()