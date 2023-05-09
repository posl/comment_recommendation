def count_ac_wa(n, m, p_s):
    ac = 0
    wa = 0
    ac_list = [0] * n
    wa_list = [0] * n
    for i in range(m):
        if p_s[i][1] == 'AC':
            if ac_list[p_s[i][0]-1] == 0:
                ac_list[p_s[i][0]-1] = 1
                ac += 1
                wa += wa_list[p_s[i][0]-1]
        else:
            if ac_list[p_s[i][0]-1] == 0:
                wa_list[p_s[i][0]-1] += 1
    return ac, wa

if __name__ == '__main__':
    count_ac_wa()