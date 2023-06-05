def get_max_num(n, a):
    a.sort(reverse=True)
    num = ''
    for i in a:
        while n >= i:
            num += str(i)
            n -= i
    return num
