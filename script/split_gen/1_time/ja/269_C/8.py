def main():
    N = int(input())
    # 2進数に変換
    N_bin = bin(N)[2:]
    # 1の位置をリストに格納
    N_bin_list = []
    for i in range(len(N_bin)):
        if N_bin[i] == '1':
            N_bin_list.append(i)
    # 1の位置の組み合わせを全て列挙
    N_bin_comb = []
    for i in range(2**len(N_bin_list)):
        bin_i = bin(i)[2:]
        bin_i = bin_i.zfill(len(N_bin_list))
        N_bin_comb.append(bin_i)
    # 組み合わせを元の1の位置に戻す
    N_bin_comb_list = []
    for i in range(len(N_bin_comb)):
        N_bin_comb_list.append([])
        for j in range(len(N_bin_comb[i])):
            if N_bin_comb[i][j] == '1':
                N_bin_comb_list[i].append(N_bin_list[j])
    # 組み合わせの要素の和が1の場合、その和を出力
    for i in range(len(N_bin_comb_list)):
        if sum(N_bin_comb_list[i]) == 1:
            print(sum(N_bin_comb_list[i]))
    # 組み合わせの要素の和が2以上の場合、その和を出力
    for i in range(len(N_bin_comb_list)):
        if sum(N_bin_comb_list[i]) >= 2:
            print(2**sum(N_bin_comb_list[i]))
