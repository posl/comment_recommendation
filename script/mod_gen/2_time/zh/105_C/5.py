def base_neg2(n):
    if n == 0:
        return "0"
    res = ""
    while n != 0:
        res = str(n & 1) + res
        n = -(n >> 1)
    return res

if __name__ == '__main__':
    base_neg2()