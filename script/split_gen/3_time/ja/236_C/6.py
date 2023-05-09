def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    # print(N, M)
    # print(S)
    # print(T)
    # 急行列車が止まる駅を集める
    stops = []
    for i in range(M):
        # print(T[i])
        for j in range(N):
            # print(S[j])
            if T[i] == S[j]:
                stops.append(j)
    # print(stops)
    # 駅の一覧を出力
    for i in range(N):
        if i in stops:
            print('Yes')
        else:
            print('No')
