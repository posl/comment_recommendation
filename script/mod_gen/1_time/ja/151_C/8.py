def get_ac_wa_count(n, m, p_s_list):
    ac_count = 0
    wa_count = 0
    ac_list = [0] * n
    wa_list = [0] * n
    for p_s in p_s_list:
        p = int(p_s[0])
        s = p_s[1]
        if ac_list[p - 1] == 0:
            if s == "AC":
                ac_count += 1
                ac_list[p - 1] = 1
                wa_count += wa_list[p - 1]
            else:
                wa_list[p - 1] += 1
    return ac_count, wa_count

if __name__ == '__main__':
    get_ac_wa_count()