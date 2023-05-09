def main():
    N = int(input())
    P = list(map(int, input().split()))
    # Pのindexを取得
    P_index = [i for i in range(N)]
    P_index = [i for i, x in sorted(zip(P_index, P), key=lambda x: x[1])]
    #print(P_index)
    # 1から順番に並べる
    Q = [i for i in range(1, N+1)]
    #print(Q)
    # Pのindexの順番にQを並び替える
    Q = [Q[i] for i in P_index]
    print(" ".join(map(str, Q)))
