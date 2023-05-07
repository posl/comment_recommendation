def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    #print(N, S, T)
    # 1. S と T を対応付けた辞書を作る
    # 2. S と T を対応付けた辞書を S でソートする
    # 3. S と T を対応付けた辞書を T でソートする
    # 4. T でソートした辞書の中で最も後ろにあるものを最優秀賞とする
    # 1. S と T を対応付けた辞書を作る
    ST = {}
    for i in range(N):
        ST[S[i]] = T[i]
    # 2. S と T を対応付けた辞書を S でソートする
    ST_sort_S = sorted(ST.items(), key=lambda x:x[0])
    #print(ST_sort_S)
    # 3. S と T を対応付けた辞書を T でソートする
    ST_sort_T = sorted(ST.items(), key=lambda x:x[1], reverse=True)
    #print(ST_sort_T)
    # 4. T でソートした辞書の中で最も後ろにあるものを最優秀賞とする
    #print(ST_sort_T[0][0])
    #print(ST_sort_S)
    for i in range(N):
        if ST_sort_T[0][0] == ST_sort_S[i][0]:
            print(i+1)
            break

if __name__ == '__main__':
    main()