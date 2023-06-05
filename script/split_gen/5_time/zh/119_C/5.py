def get_min_mp(N, A, B, C, l_list):
    if A in l_list and B in l_list and C in l_list:
        return 0
    mp = 100000
    for i in range(3**N):
        a = A
        b = B
        c = C
        mp_tmp = 0
        for j in range(N):
            if i % 3 == 0:
                a -= l_list[j]
                mp_tmp += 10
            elif i % 3 == 1:
                b -= l_list[j]
                mp_tmp += 10
            else:
                c -= l_list[j]
                mp_tmp += 10
            i = int(i / 3)
        if a == 0 and b == 0 and c == 0:
            mp = min(mp, mp_tmp)
    return mp
