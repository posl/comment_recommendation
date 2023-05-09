def main():
    #入力
    N, M = map(int, input().split())
    P = [0 for i in range(M)]
    Y = [0 for i in range(M)]
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #市の誕生年の昇順にソート
    #ソート前の市の番号を保持
    P_sort = sorted(P)
    Y_sort = sorted(Y)
    P_num = [0 for i in range(M)]
    for i in range(M):
        P_num[i] = P.index(P_sort[i])
    #市の誕生年をソート
    Y_sort = sorted(Y)
    #県の市の数をカウント
    P_count = [0 for i in range(N)]
    for i in range(M):
        P_count[P[i]-1] += 1
    #県の市の数を累積和
    P_count = [0] + P_count
    for i in range(N):
        P_count[i+1] += P_count[i]
    #市の認識番号を出力
    for i in range(M):
        print('{0:06d}'.format(P_sort[i]) + '{0:06d}'.format(P_count[P_sort[i]-1] - P_count[P_sort[i]-2] - (Y_sort.index(Y[P_num[i]]) - P_count[P_sort[i]-1] + M)))

if __name__ == '__main__':
    main()