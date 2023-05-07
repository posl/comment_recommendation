def main():
    #入力
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    #a = [list(map(int, input().split())) for i in range(H)]
    #処理
    #行列の転置
    a = list(map(list, zip(*a)))
    #print(a)
    #行列の転置
    a = list(map(list, zip(*a)))
    #print(a)
    #出力
    for i in range(H):
        for j in range(W):
            print(a[i][j], end="")
        print("")
