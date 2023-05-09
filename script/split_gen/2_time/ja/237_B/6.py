def main():
    #入力
    H, W = map(int, input().split())
    #A = [list(map(int, input().split())) for i in range(H)]
    A = [input().split() for i in range(H)]
    #B = [[0]*H for i in range(W)]
    #転置行列を作成
    B = list(zip(*A))
    #出力
    for i in range(W):
        print(" ".join(B[i]))
