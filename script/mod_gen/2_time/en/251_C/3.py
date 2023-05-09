def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    #print(S)
    #print(T)
    # 既出の文字列を記録
    S_set = set()
    # 各文字列の最高得点を記録
    T_max = {}
    # 各文字列の最高得点を記録したSubmissionのインデックスを記録
    T_max_index = {}
    for i in range(N):
        if S[i] not in S_set:
            S_set.add(S[i])
            T_max[S[i]] = T[i]
            T_max_index[S[i]] = i
        else:
            if T[i] > T_max[S[i]]:
                T_max[S[i]] = T[i]
                T_max_index[S[i]] = i
    #print(S_set)
    #print(T_max)
    #print(T_max_index)
    # 各文字列の最高得点を記録したSubmissionのインデックスのうち、最小のものを探す
    T_max_index_min = N
    for s in S_set:
        T_max_index_min = min(T_max_index_min, T_max_index[s])
    print(T_max_index_min + 1)

if __name__ == '__main__':
    main()