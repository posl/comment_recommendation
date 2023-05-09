def main():
    N = int(input())
    
    # N の 2 進数表記の 1 の位置を求める
    N_bin = bin(N)[2:]
    N_bin_len = len(N_bin)
    N_bin_1_pos = []
    for i in range(N_bin_len):
        if N_bin[N_bin_len-i-1] == '1':
            N_bin_1_pos.append(i)
    
    # 1 の位置の組み合わせを列挙する
    N_bin_1_pos_comb = []
    for i in range(2**len(N_bin_1_pos)):
        bin_i = bin(i)[2:].zfill(len(N_bin_1_pos))
        comb = []
        for j in range(len(N_bin_1_pos)):
            if bin_i[j] == '1':
                comb.append(N_bin_1_pos[j])
        N_bin_1_pos_comb.append(comb)
    
    # 1 の位置の組み合わせをもとに x を求める
    for comb in N_bin_1_pos_comb:
        x = 0
        for pos in comb:
            x += 2**pos
        print(x)

if __name__ == '__main__':
    main()