def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M)
    #print(X)
    # 前から順に移動する場合の最小移動回数
    #print("前から順に移動する場合の最小移動回数")
    move = 0
    for i in range(M-1):
        move += X[i+1] - X[i]
    #print(move)
    # 後ろから順に移動する場合の最小移動回数
    #print("後ろから順に移動する場合の最小移動回数")
    move2 = 0
    for i in range(M-1, 0, -1):
        move2 += X[i] - X[i-1]
    #print(move2)
    # コマの数が多い場合は、移動しないコマを移動させる
    if N >= M:
        print(0)
    else:
        print(move - move2)
