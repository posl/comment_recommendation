def num2str(num):
    res = ""
    while num > 0:
        num, mod = divmod(num, 26)
        if mod == 0:
            res = "z" + res
            num -= 1
        else:
            res = chr(ord("a") + mod - 1) + res
    return res

if __name__ == '__main__':
    num2str()