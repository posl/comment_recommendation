def calc(n):
    res = n
    for a in range(100):
        for b in range(100):
            res = min(res, a**3 + a**2*b + a*b**2 + b**3)
    return res

if __name__ == '__main__':
    calc()