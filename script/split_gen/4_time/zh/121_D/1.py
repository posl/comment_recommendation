def cal_xor(a,b):
    if a==b:
        return a
    else:
        return cal_xor(a,b-1)^b
