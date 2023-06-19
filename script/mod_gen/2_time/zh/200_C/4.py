def get200(n, a):
    a.sort()
    a_dic = {}
    for i in a:
        if i % 200 in a_dic:
            a_dic[i % 200] += 1
        else:
            a_dic[i % 200] = 1
    res = 0
    for i in a_dic:
        res += a_dic[i] * (a_dic[i] - 1) / 2
    return res

if __name__ == '__main__':
    get200()