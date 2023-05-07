def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    # 1からNまでの宝石の数をリストに格納する
    # 1からNまでの宝石の数をリストに格納する
    gem = [0] * (N + 1)
    gem[1] = 1
    #print(gem)
    # 1からNまでの宝石の数をリストに格納する
    for i in range(1, N):
        gem[i + 1] = gem[i] * X + gem[i - 1] * Y
    #print(gem)
    # 答えを出力する
    print(gem[N])
