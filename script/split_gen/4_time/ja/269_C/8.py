def main():
    N = int(input())
    # Nの2進数表記の1の位の集合を求める
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_bin = N_bin[::-1]
    N_bin = [i for i, x in enumerate(N_bin) if x == "1"]
    #print(N_bin)
    # 1の位の集合の部分集合を求める
    ans = []
    for i in range(2**len(N_bin)):
        tmp = []
        for j in range(len(N_bin)):
            if ((i >> j) & 1):
                tmp.append(N_bin[j])
        ans.append(tmp)
    #print(ans)
    # 2進数の1の位の集合から10進数を求めて出力
    for i in range(len(ans)):
        tmp = 0
        for j in range(len(ans[i])):
            tmp += 2**ans[i][j]
        print(tmp)
