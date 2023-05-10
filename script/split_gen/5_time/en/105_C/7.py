def base_neg2(n):
    if n == 0:
        return "0"
    ret = ""
    while n != 0:
        if n % 2 == 0:
            ret += "0"
        else:
            ret += "1"
            n -= 1
        n //= -2
    return ret[::-1]
