def main():
    N, M = map(int, input().split())
    # 都市のリスト
    city = [i for i in range(1,N+1)]
    # 道路のリスト
    road = []
    for i in range(M):
        A, B = map(int, input().split())
        road.append([A,B])
    # 道路のリストを、都市1から都市2への辺のリストに変換
    # road[0][0] = A_i
    # road[0][1] = B_i
    # road[1][0] = A_j
    # road[1][1] = B_j
    # road[2][0] = A_k
    # road[2][1] = B_k
    # road[3][0] = A_l
    # road[3][1] = B_l
    # road[4][0] = A_m
    # road[4][1] = B_m
    # road[5][0] = A_n
    # road[5][1] = B_n
    # road[6][0] = A_o
    # road[6][1] = B_o
    # road[7][0] = A_p
    # road[7][1] = B_p
    # road[8][0] = A_q
    # road[8][1] = B_q
    # road[9][0] = A_r
    # road[9][1] = B_r
    # road[10][0] = A_s
    # road[10][1] = B_s
    # road[11][0] = A_t
    # road[11][1] = B_t
    # road[12][0] = A_u
    # road[12][1] = B_u
    # road[13][0] = A_v
    # road[13][1] = B_v
    # road[14][0] = A_w
    # road[14][1] = B_w
    # road[15][0] = A_x
    # road[15][1] = B_x
    # road[16][

if __name__ == '__main__':
    main()