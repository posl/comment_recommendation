def get_num(n, m, s_c):
    if n == 1:
        if s_c[0][0] == 1:
            return s_c[0][1]
        else:
            return -1
    elif n == 2:
        if s_c[0][0] == 1 and s_c[1][0] == 2:
            return s_c[0][1]*10 + s_c[1][1]
        else:
            return -1
    else:
        if s_c[0][0] == 1 and s_c[1][0] == 2 and s_c[2][0] == 3:
            return s_c[0][1]*100 + s_c[1][1]*10 + s_c[2][1]
        else:
            return -1
