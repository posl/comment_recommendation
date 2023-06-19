def problems210_c():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    c_dict = {}
    for i in range(K):
        if c[i] in c_dict:
            c_dict[c[i]] += 1
        else:
            c_dict[c[i]] = 1
    c_dict_len = len(c_dict)
    c_dict_len_max = c_dict_len
    for i in range(K,N):
        if c[i] in c_dict:
            c_dict[c[i]] += 1
        else:
            c_dict[c[i]] = 1
            c_dict_len += 1
        c_dict[c[i-K]] -= 1
        if c_dict[c[i-K]] == 0:
            c_dict_len -= 1
        if c_dict_len_max < c_dict_len:
            c_dict_len_max = c_dict_len
    print(c_dict_len_max)
problems210_c()
