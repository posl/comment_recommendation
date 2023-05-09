def main():
    N = int(input())
    N_bin = format(N, 'b')
    N_len = len(N_bin)
    N_list = []
    for i in range(N_len):
        if N_bin[i] == '1':
            N_list.append(i)
    #print(N_list)
    for i in range(2**len(N_list)):
        tmp_bin = format(i, 'b')
        tmp_len = len(tmp_bin)
        tmp_list = []
        for j in range(tmp_len):
            if tmp_bin[j] == '1':
                tmp_list.append(j)
        #print(tmp_list)
        if set(tmp_list) <= set(N_list):
            print(i)
