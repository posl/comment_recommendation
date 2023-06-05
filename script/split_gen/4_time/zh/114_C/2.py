def check753(num):
    check = set(['3','5','7'])
    num_str = str(num)
    for i in check:
        if i not in num_str:
            return False
    return True
