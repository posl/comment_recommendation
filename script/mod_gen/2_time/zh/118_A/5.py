def f(x, a_list):
    res = 0
    for a in a_list:
        res += x ^ a
    return res

if __name__ == '__main__':
    f()