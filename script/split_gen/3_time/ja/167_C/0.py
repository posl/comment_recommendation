def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)
    import itertools
    # 2**N通りの組み合わせを全探索
    # それぞれの組み合わせについて、アルゴリズムの理解度を計算する
    # その中から、理解度がX以上のものを探す
    # その中で、最もコストが小さいものを求める
    # 2**N通りの組み合わせを全探索
    min_cost = 10**9
    for i in range(2**N):
        #print(i)
        # 2進数に変換
        bin_i = bin(i)[2:]
        #print(bin_i)
        # 左詰めにする
        bin_i = bin_i.zfill(N)
        #print(bin_i)
        #print(bin_i[0])
        #print(bin_i[1])
        # それぞれの組み合わせについて、アルゴリズムの理解度を計算する
        # それぞれの理解度を0で初期化
        a = [0] * M
        #print(a)
        cost = 0
        for j in range(N):
            #print(j)
            #print(bin_i[j])
            if bin_i[j] == "1":
                #print("1")
                #print(j)
                #print(C[j])
                cost += C[j]
                #print(a)
                #print(A[j])
                for k in range(M):
                    #print(k)
                    #print(A[j][k])
                    a[k] += A[j][k]
                    #print(a)
        #print(a)
        # その中から、理解度がX以上のものを探す
        is_ok = True
        for j in range(M):
            if a[j] < X:
