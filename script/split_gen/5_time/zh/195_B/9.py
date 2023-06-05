def get_orange_num(a, b, w):
    min_num = 0
    max_num = 0
    if a > w or w > b:
        return 'UNSATISFIABLE'
    #最小值
    if w % a == 0:
        min_num = w // a
    else:
        min_num = w // a + 1
    #最大值
    max_num = w // b
    return str(min_num) + ' ' + str(max_num)
