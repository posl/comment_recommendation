def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    # 各人の移動方向を初期化
    dir = [0] * N
    for i, s in enumerate(S):
        if s == 'R':
            dir[i] = 1
        else:
            dir[i] = -1
    # 各人の移動先を初期化
    X = [0] * N
    Y = [0] * N
    for i, xy in enumerate(XY):
        X[i] = xy[0]
        Y[i] = xy[1]
    # 各人の移動先を計算
    for i in range(N):
        X[i] += dir[i]
        Y[i] += dir[i]
    # 移動先の座標でソート
    X.sort()
    Y.sort()
    # 移動先の座標が同じ人がいたら衝突する
    for i in range(N-1):
        if X[i] == X[i+1] or Y[i] == Y[i+1]:
            print('Yes')
            exit()
    # 衝突しなかったら衝突しない
    print('No')

if __name__ == '__main__':
    solve()