def convert_base(n, base):
    if n == 0:
        return "0"
    ret = ""
    while n > 0:
        ret += str(n % base)
        n //= base
    return ret[::-1]
