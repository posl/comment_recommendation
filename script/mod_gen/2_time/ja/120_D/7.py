def main():
    N, M = map(int, input().split())
    bridge = [tuple(map(int, input().split())) for _ in range(M)]
    #print(bridge)
    #print(N, M)
    #print(bridge)
    #print(bridge[0][0])
    #print(bridge[0][1])
    #不便さの初期値は0
    inconvenience = 0
    #島の数を初期化
    island = [0] * (N + 1)
    #島の数の初期値は1
    for i in range(1, N + 1):
        island[i] = 1
    #print(island)
    #橋の個数を初期化
    bridge_num = [0] * (N + 1)
    #橋の個数の初期値は0
    for i in range(1, N + 1):
        bridge_num[i] = 0
    #print(bridge_num)
    #不便さの初期値を計算
    for i in range(1, N + 1):
        inconvenience += (island[i] * (island[i] - 1)) // 2
    #print(inconvenience)
    #不便さを出力
    print(inconvenience)
    #橋の個数を計算
    for i in range(M):
        bridge_num[bridge[i][0]] += 1
        bridge_num[bridge[i][1]] += 1
    #print(bridge_num)
    #橋の個数を用いて不便さを計算
    for i in range(M):
        inconvenience -= (island[bridge[i][0]] * (island[bridge[i][0]] - 1)) // 2
        inconvenience -= (island[bridge[i][1]] * (island[bridge[i][1]] - 1)) // 2
        island[bridge[i][0]] += 1
        island[bridge[i][1]] += 1
        inconvenience += (island[bridge[i][0]] * (island[bridge[i][0]] - 1)) // 2

if __name__ == '__main__':
    main()