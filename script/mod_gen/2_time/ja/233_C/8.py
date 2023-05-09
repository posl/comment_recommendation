def main():
    #入力
    N, X = map(int, input().split())
    #N 個の袋の情報を入れるリスト
    bag = []
    #N 個の袋の情報を入力
    for i in range(N):
        bag.append(list(map(int, input().split())))
    #袋 i の j 番目のボールに書かれた数の総積が X になる取り出し方の個数
    ans = 0
    #袋 i の j 番目のボールを選ぶか選ばないかの全探索
    for i in range(2 ** N):
        #袋 i の j 番目のボールを選ぶか選ばないかのフラグ
        flag = [0] * N
        #袋 i の j 番目のボールを選ぶか選ばないかのフラグの設定
        for j in range(N):
            if (i >> j) & 1:
                flag[j] = 1
        #袋 i の j 番目のボールに書かれた数の総積
        mul = 1
        #袋 i の j 番目のボールに書かれた数の総積の計算
        for j in range(N):
            if flag[j] == 1:
                mul *= bag[j][1 + flag[j]]
        #袋 i の j 番目のボールに書かれた数の総積が X になる取り出し方の個数の計算
        if mul == X:
            ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()