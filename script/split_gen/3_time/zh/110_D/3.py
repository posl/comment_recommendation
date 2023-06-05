def get_divisor(num):
    ret = []
    for i in range(1,num+1):
        if num % i == 0:
            ret.append(i)
    return ret
