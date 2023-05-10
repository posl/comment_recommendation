def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(AB)
    # 部屋の道しるべの番号を格納するリスト
    roadsign = [0] * N
    # 1 からの道しるべを出力
    print('Yes')
    print(1)
    # 部屋 1 以外の道しるべを出力
    # 1 からの道しるべを出力したので、
    # 2 から N までの道しるべを出力
    for i in range(2, N+1):
        print(roadsign[i-1])
        # 道しるべが指す部屋の番号を格納する変数
        # 道しるべが指す部屋の番号は、
        # その部屋と通路で直接つながっている部屋の 1 つ
        roadsign[i-1] = AB[i-2][0]
    # print(roadsign)
