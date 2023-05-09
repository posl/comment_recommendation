def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #print(N)
    #print(P)
    #print(Q)
    #print(len(P))
    #print(len(Q))
    #print(P[0])
    #print(Q[0])
    #順列を作成
    #Pの順列を作成
    P_array = []
    for i in range(N):
        P_array.append(i+1)
    #print(P_array)
    #Qの順列を作成
    Q_array = []
    for i in range(N):
        Q_array.append(i+1)
    #print(Q_array)
    #P,Qの順列を作成
    import itertools
    P_permutations = list(itertools.permutations(P_array))
    #print(P_permutations)
    Q_permutations = list(itertools.permutations(Q_array))
    #print(Q_permutations)
    #P,Qの順列を辞書順にソート
    P_permutations.sort()
    #print(P_permutations)
    Q_permutations.sort()
    #print(Q_permutations)
    #P,Qの順列が何番目にあるかを取得
    P_count = 0
    Q_count = 0
    for i in range(len(P_permutations)):
        if P_permutations[i] == tuple(P):
            P_count = i + 1
    #print(P_count)
    for i in range(len(Q_permutations)):
        if Q_permutations[i] == tuple(Q):
            Q_count = i + 1
    #print(Q_count)
    #|a - b|を出力
    print(abs(P_count - Q_count))

if __name__ == '__main__':
    main()