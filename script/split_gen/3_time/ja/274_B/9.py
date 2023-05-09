def main():
    #入力
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    #print(H, W, C)
    #処理
    #X_j = j 列目に置かれている箱の個数
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    #出力
    print(*X)
