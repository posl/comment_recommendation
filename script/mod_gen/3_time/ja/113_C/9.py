def main():
    N, M = map(int, input().split())
    #県の市の数を格納するリスト
    city = [0] * N
    #市の認識番号を格納するリスト
    num = [0] * M
    for i in range(M):
        P, Y = map(int, input().split())
        #県の市の数をインクリメント
        city[P - 1] += 1
        #市の認識番号を生成
        num[i] = str(P).zfill(6) + str(city[P - 1]).zfill(6)
    #市の認識番号を出力
    for i in range(M):
        print(num[i])

if __name__ == '__main__':
    main()